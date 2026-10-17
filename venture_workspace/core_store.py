"""Server-side, read-only Designeo OS Core adapter for Venture Workspace.

Core state is the canonical source. This adapter cannot write, approve gates,
execute actions or authenticate clients. No credentials are exposed to the UI.
"""
from __future__ import annotations

import json
import re
from copy import deepcopy
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, HTTPHandler, Request, build_opener

SCOPE = "venture-factory"
SCHEMA = "designeo.venture.candidate.v0.1"
ENDPOINT = "/v1/system/state?scope=venture-factory"
ID_RE = re.compile(r"^VF-[A-Z0-9-]{3,64}$")
MAX_RESPONSE_BYTES = 1_000_000


class WorkspaceError(ValueError):
    """Safe operational error; never attach HTTP bodies or credentials."""


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise WorkspaceError("Core redirect refused")


def parse_candidates(rows: list[dict]) -> list[dict]:
    """Select canonical candidates; reject duplicate IDs and malformed UI fields.

    A source's validation claim is kept as *reported state*, never presented as
    independently verified business validation. No type is silently coerced.
    """
    if not isinstance(rows, list):
        raise WorkspaceError("Core returned an invalid candidate list")
    results: list[dict] = []
    ids = set()
    for item in rows:
        if not isinstance(item, dict) or item.get("scope") != SCOPE:
            continue
        value = item.get("value")
        key = item.get("key")
        if not isinstance(value, dict) or not isinstance(key, str):
            continue
        if value.get("schema") != SCHEMA:
            continue
        cid = value.get("id")
        if not isinstance(cid, str) or not ID_RE.fullmatch(cid) or key != "candidate:" + cid:
            continue
        if cid in ids:
            raise WorkspaceError("Duplicate canonical candidate ID returned by Core")
        for name in ("name", "stage", "problem", "value_proposition"):
            if name in value and (not isinstance(value[name], str) or len(value[name]) > 3000):
                raise WorkspaceError("Candidate contains an invalid descriptive field")
        for name in ("customer_segments", "hypotheses", "risks"):
            vals = value.get(name, [])
            if not isinstance(vals, list) or len(vals) > 100 or any(
                    not isinstance(v, str) or len(v) > 3000 for v in vals):
                raise WorkspaceError("Candidate contains an invalid collection")
        if not isinstance(value.get("experiments", []), list):
            raise WorkspaceError("Candidate contains invalid experiments")
        if not isinstance(value.get("metrics", {}), dict) or not isinstance(value.get("costs", {}), dict):
            raise WorkspaceError("Candidate contains invalid metrics")
        ids.add(cid)
        v = deepcopy(value)
        v["_updated_at"] = item.get("updated_at", "")
        results.append(v)
    return sorted(results, key=lambda x: (x.get("name", "").casefold(), x["id"]))


def summary(candidates: list[dict]) -> dict:
    """Aggregate discovery status, not unverifiable commercial achievements."""
    return {
        "total": len(candidates),
        "in_discovery": sum(c.get("stage", "").startswith("G0") for c in candidates),
        "validation_claims": sum(c.get("business_validated") is True for c in candidates),
        "pending_experiments": sum(
            e.get("status") in ("planned", "not_started", "blocked_security_gate")
            for c in candidates for e in c.get("experiments", [])
            if isinstance(e, dict)
        ),
    }


class CoreStateStore:
    """Read-only internal transport; works with trusted server-only credentials.

    Core's current global Bearer credential is NOT project-scoped authorization.
    Keep this behind a private network boundary. No write endpoint is invoked.
    """

    def __init__(self, base_url: str, token: str):
        if not isinstance(base_url, str) or not isinstance(token, str):
            raise WorkspaceError("Core configuration is incomplete")
        parts = urlsplit(base_url)
        is_loopback = parts.scheme == "http" and parts.hostname in {
            "localhost", "127.0.0.1", "::1"
        }
        if not ((parts.scheme == "https" or is_loopback) and parts.hostname):
            raise WorkspaceError("Core address must use HTTPS or loopback")
        if (parts.username or parts.password or parts.query or parts.fragment
                or parts.path not in ("", "/")):
            raise WorkspaceError("Core base URL cannot contain credentials, paths or queries")
        if not token.strip() or "\n" in token or "\r" in token:
            raise WorkspaceError("Valid server-only Core token is required")
        self.base = base_url.rstrip("/")
        self._token = token
        self._opener = build_opener(_NoRedirect(), HTTPSHandler(), HTTPHandler())

    def list_candidates(self) -> list[dict]:
        """One allowlisted GET, bounded response, no fallback or broad Core listing."""
        request = Request(self.base + ENDPOINT,
                          method="GET",
                          headers={"Authorization": "Bearer " + self._token,
                                   "Accept": "application/json"})
        try:
            with self._opener.open(request, timeout=8) as response:
                content = response.read(MAX_RESPONSE_BYTES + 1)
        except HTTPError as exc:
            raise WorkspaceError(f"Core returned HTTP {exc.code}") from None
        except URLError:
            raise WorkspaceError("Core unavailable") from None
        if len(content) > MAX_RESPONSE_BYTES:
            raise WorkspaceError("Core candidate response exceeds size limit")
        try:
            payload = json.loads(content.decode("utf-8"))
        except (UnicodeError, ValueError):
            raise WorkspaceError("Core returned invalid JSON") from None
        return parse_candidates(payload)

    def update_candidate(self, *args, **kwargs):
        """Explicitly disabled pending a reviewed atomic revision API."""
        raise WorkspaceError("Workspace writes are disabled until Core revisions are approved")
