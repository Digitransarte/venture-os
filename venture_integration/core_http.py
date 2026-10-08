"""Optional Designeo OS Core REST transport for the VentureCoreJournal.

No network actions occur at import or construction time. Caller provides the
Core API token at runtime; never commit it, log it, or embed it in a fixture.
"""
from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import (
    HTTPRedirectHandler, HTTPSHandler, HTTPHandler, Request,
    build_opener,
)


class CoreTransportError(RuntimeError):
    """HTTP transport failed (message deliberately excludes tokens and body)."""


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
            raise CoreTransportError(f"Core API returned HTTP {err.code}") from None
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
