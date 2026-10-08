"""Optional Designeo OS Core REST transport for the VentureCoreJournal.

No network actions occur at import or construction time. Caller provides the
Core API token at runtime; never commit it, log it, or embed it in a fixture.
"""
from __future__ import annotations

import json
from typing import Any
from . import SNAPSHOT_KIND, fingerprint, validate
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import (
    HTTPRedirectHandler, HTTPSHandler, HTTPHandler, Request,
    build_opener,
)


class CoreTransportError(RuntimeError):
    """HTTP transport error; messages exclude credentials and response bodies."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise CoreTransportError("Redirect refused for Core API request")


class CoreMemoryHttpAdapter:
    """Small adapter for /v1/projects/{slug}/memory.

    Project entity must exist before using this adapter. Snapshots are
    append-only, not atomic: concurrent writers need server-side uniqueness.
    """

    def __init__(self, *, base_url: str, api_token: str,
                 project_slug: str, timeout: int = 10):
        parts = urlsplit(base_url)
        is_local = parts.scheme == "http" and parts.hostname in {"localhost", "127.0.0.1", "::1"}
        if (parts.scheme != "https" and not is_local) or not parts.hostname:
            raise ValueError("Core base_url must be HTTPS (except loopback testing)")
        if parts.username or parts.password or parts.query or parts.fragment:
            raise ValueError("Do not include credentials, query or fragments in URL")
        if not isinstance(api_token, str) or not api_token.strip():
            raise ValueError("Core API token is required")
        if not project_slug or "/" in project_slug:
            raise ValueError("A valid Core project slug is required")
        if timeout < 1 or timeout > 60:
            raise ValueError("Timeout must be between 1 and 60 seconds")
        self._base = base_url.rstrip("/")
        self._token = api_token
        self.project_slug = project_slug
        self._timeout = timeout
        self._opener = build_opener(_NoRedirect(), HTTPHandler(), HTTPSHandler())

    def _request(self, method: str, path: str, payload: dict | None = None) -> Any:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
        headers = {"Authorization": "Bearer " + self._token, "Accept": "application/json"}
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = Request(self._base + path, data=data, headers=headers, method=method)
        try:
            with self._opener.open(request, timeout=self._timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as err:
            raise CoreTransportError(f"Core API returned HTTP {err.code}", status_code=err.code) from None
        except URLError:
            raise CoreTransportError("Core API unavailable") from None
        except (UnicodeError, json.JSONDecodeError):
            raise CoreTransportError("Core API returned invalid JSON") from None

    def _memory_path(self) -> str:
        return "/v1/projects/" + quote(self.project_slug, safe="") + "/memory"

    def list_memory(self, kind: str, ref: str) -> list[dict]:
        query = urlencode({"kind": kind, "q": ref, "limit": 500})
        value = self._request("GET", self._memory_path() + "?" + query)
        if not isinstance(value, list):
            raise CoreTransportError("Core Memory list has unexpected format")
        return value

    def add_memory(self, entry: dict) -> dict:
        if entry.get("kind") == SNAPSHOT_KIND:
            raise CoreTransportError("Versioned snapshots require append_atomic")
        payload = {field: entry[field] for field in ("title", "kind", "content", "tags") if field in entry}
        value = self._request("POST", self._memory_path(), payload)
        if not isinstance(value, dict) or not value.get("id"):
            raise CoreTransportError("Core did not confirm Memory ID")
        return value

    def get_project(self) -> dict:
        value = self._request("GET", "/v1/projects/" + quote(self.project_slug, safe=""))
        if not isinstance(value, dict) or value.get("slug") != self.project_slug:
            raise CoreTransportError("Core Project mismatch")
        return value

    def get_latest(self, venture_ref: str) -> dict | None:
        """Read the authoritative Core revision. Return None only on 404."""
        endpoint = ("/v1/projects/" + quote(self.project_slug, safe="")
                    + "/venture-records/" + quote(venture_ref, safe=""))
        try:
            value = self._request("GET", endpoint)
        except CoreTransportError as exc:
            if exc.status_code == 404:
                return None
            raise
        if not isinstance(value, dict) or value.get("revision", 0) < 1:
            raise CoreTransportError("Core returned invalid Venture Record")
        if not isinstance(value.get("record"), dict):
            raise CoreTransportError("Core returned invalid Venture content")
        if value.get("digest") != fingerprint(value["record"]):
            raise CoreTransportError("Core Venture Record hash mismatch")
        return value

    def append_atomic(
        self, record: dict, *, expected_revision: int, expected_digest: str | None
    ) -> dict:
        """Use the new Core transactional compare-and-swap endpoint.

        No request is made when validation or tenant binding fails.
        Conflict responses (409) must be handled by refreshing latest state.
        """
        obj = validate(record)
        if obj["core_project_slug"] != self.project_slug:
            raise CoreTransportError("Cross-project Venture Record write refused")
        if type(expected_revision) is not int or expected_revision < 0:
            raise CoreTransportError("Invalid expected_revision")
        if expected_revision == 0 and expected_digest is not None:
            raise CoreTransportError("First revision cannot have predecessor")
        if expected_revision > 0 and (
            not isinstance(expected_digest, str)
            or len(expected_digest) != 64
            or any(ch not in "0123456789abcdef" for ch in expected_digest)
        ):
            raise CoreTransportError("Expected predecessor digest required")
        endpoint = ("/v1/projects/" + quote(self.project_slug, safe="")
                    + "/venture-records/" + quote(obj["venture_ref"], safe="")
                    + "/revisions")
        value = self._request("POST", endpoint, {
            "record": obj, "expected_revision": expected_revision,
            "expected_digest": expected_digest,
        })
        if not isinstance(value, dict) or value.get("digest") != fingerprint(obj):
            raise CoreTransportError("Core did not confirm matching Venture Record")
        if value.get("status") not in {"created", "unchanged"} or not value.get("memory_id"):
            raise CoreTransportError("Core did not confirm a valid journal revision")
        return value
