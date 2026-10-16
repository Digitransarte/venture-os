"""Private internal Venture Workspace data adapter.

The Designeo OS Core remains the source of truth. No local candidate database,
no token in browser code, and no public/multitenant authentication contract.
"""
from __future__ import annotations

import json
import re
from copy import deepcopy
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, HTTPHandler, Request, build_opener

SCOPE = "venture-factory"
SCHEMA = "designeo.venture.candidate.v0.1"
ID_RE = re.compile(r"^VF-[A-Z0-9-]{3,64}$")
EDITABLE = frozenset({"problem", "value_proposition", "next_action", "notes"})
MAX_TEXT = 3000


class WorkspaceError(ValueError):
    pass


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise WorkspaceError("Core redirect refused")


def parse_candidates(rows: list[dict]) -> list[dict]:
    """Read Core system_state candidate records; ignore unrelated records."""
    output = []
    for item in rows:
        if not isinstance(item, dict) or item.get("scope") != SCOPE:
            continue
        value = item.get("value")
        key = item.get("key", "")
        if not isinstance(value, dict) or not isinstance(key, str):
            continue
        if value.get("schema") != SCHEMA:
            continue
        candidate_id = value.get("id")
        if not isinstance(candidate_id, str) or not ID_RE.fullmatch(candidate_id):
            continue
        if key != "candidate:" + candidate_id:
            continue
        output.append({**deepcopy(value), "_updated_at": item.get("updated_at", "")})
    return sorted(output, key=lambda item: (item.get("name", "").casefold(), item["id"]))


def patch_candidate(original: dict, patch: dict) -> dict:
    """Allow editing text hypotheses only; never grant gates or market validation."""
    if not isinstance(original, dict) or original.get("schema") != SCHEMA:
        raise WorkspaceError("Invalid candidate")
    if not isinstance(patch, dict) or not patch or set(patch) - EDITABLE:
        raise WorkspaceError("Only non-authorizing descriptive fields may be edited")
    candidate = deepcopy(original)
    candidate.pop("_updated_at", None)
    for key, value in patch.items():
        if not isinstance(value, str) or len(value) > MAX_TEXT:
            raise WorkspaceError(f"Invalid text for {key}")
        candidate[key] = value.strip()
    return candidate


def summary(candidates: list[dict]) -> dict:
    return {
        "total": len(candidates),
        "in_discovery": sum(c.get("stage", "").startswith("G0") for c in candidates),
        "validated_businesses": sum(c.get("business_validated") is True for c in candidates),
        "pending_experiments": sum(
            e.get("status") in ("planned", "not_started", "blocked_security_gate")
            for c in candidates for e in c.get("experiments", [])
            if isinstance(e, dict)
        ),
    }


class CoreStateStore:
    """Server-only trusted Core transport. Never expose Core token to a browser.

    The existing Core /system/state PUT is *not* atomic compare-and-swap:
    writes are disabled by default, require a single trusted admin, and must
    migrate to Venture revisions before multi-editor use.
    """

    def __init__(self, base_url: str, token: str, *, allow_legacy_writes: bool = False):
        url = urlsplit(base_url)
        local = url.scheme == "http" and url.hostname in {"127.0.0.1", "localhost", "::1"}
        if not ((url.scheme == "https" or local) and url.hostname):
            raise WorkspaceError("Core address must use HTTPS or loopback")
        if url.username or url.password or url.query or url.fragment:
            raise WorkspaceError("Credentials or URL query are forbidden")
        if not token or not isinstance(token, str):
            raise WorkspaceError("Server-only Core token required")
        self.base = base_url.rstrip("/")
        self.token = token
        self.allow_legacy_writes = allow_legacy_writes
        self.opener = build_opener(_NoRedirect(), HTTPSHandler(), HTTPHandler())

    def _request(self, method: str, path: str, body: dict | None = None):
        payload = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
        headers = {"Authorization": "Bearer " + self.token, "Accept": "application/json"}
        if payload is not None:
            headers["Content-Type"] = "application/json"
        request = Request(self.base + path, data=payload, method=method, headers=headers)
        try:
            with self.opener.open(request, timeout=8) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as err:
            raise WorkspaceError(f"Core returned HTTP {err.code}") from None
        except URLError:
            raise WorkspaceError("Core unavailable") from None
        except (UnicodeError, ValueError):
            raise WorkspaceError("Core returned invalid JSON") from None

    def list_candidates(self) -> list[dict]:
        result = self._request("GET", "/v1/system/state?scope=" + SCOPE)
        if not isinstance(result, list):
            raise WorkspaceError("Core returned invalid candidate listing")
        return parse_candidates(result)

    def update_candidate(self, candidate_id: str, expected_updated_at: str, patch: dict) -> dict:
        if not self.allow_legacy_writes:
            raise WorkspaceError("Workspace writes disabled pending reviewed Core revision API")
        if not ID_RE.fullmatch(candidate_id or "") or not expected_updated_at:
            raise WorkspaceError("Candidate identity and version are required")
        # Single-admin read-before-write check is a safeguard, NOT atomic CAS.
        listing = self._request("GET", "/v1/system/state?scope=" + SCOPE)
        row = next((x for x in listing if x.get("key") == "candidate:" + candidate_id
                    and x.get("scope") == SCOPE), None)
        if not row or row.get("updated_at") != expected_updated_at:
            raise WorkspaceError("Candidate changed: refresh before editing")
        changed = patch_candidate(row["value"], patch)
        path = "/v1/system/state/" + SCOPE + "/" + quote("candidate:" + candidate_id, safe="")
        response = self._request("PUT", path, {
            "value": changed,
            "state_type": row.get("state_type", "venture_candidate"),
            "provenance": "declared",
            "source": "venture-workspace-v0.1; internal admin edit",
            "confidence": row.get("confidence"),
        })
        if not isinstance(response, dict) or response.get("value", {}).get("id") != candidate_id:
            raise WorkspaceError("Core did not confirm updated candidate")
        return response
