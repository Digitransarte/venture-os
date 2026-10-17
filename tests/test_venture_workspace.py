"""Regressions for the read-only Venture Workspace / Designeo Core contract.

HTTP calls are deliberately mocked: no live Core secrets or endpoints are used.
"""
import json
import unittest
from unittest.mock import Mock
from urllib.error import URLError

from venture_workspace.core_store import (
    CoreStateStore, ENDPOINT, MAX_RESPONSE_BYTES,
    WorkspaceError, parse_candidates, summary,
)

BASE = {
    "scope": "venture-factory", "key": "candidate:VF-DEMO-01",
    "updated_at": "2026-10-16T10:00:00Z",
    "state_type": "venture_candidate", "provenance": "declared",
    "source": "test", "confidence": None,
    "value": {
        "schema": "designeo.venture.candidate.v0.1",
        "id": "VF-DEMO-01", "name": "Synthetic project",
        "stage": "G0_discovery", "problem": "Initial hypothesis",
        "experiments": [{"name": "Interview", "status": "planned"}],
        "business_validated": False,
    },
}
SECOND = {
    **BASE, "key": "candidate:VF-TEST-02",
    "value": {
        **BASE["value"], "id": "VF-TEST-02", "name": "Another synthetic project",
        "experiments": [],
    },
}


class FakeResponse:
    def __init__(self, payload):
        self.content = payload
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    def read(self, count):
        return self.content[:count]


class WorkspaceCoreTests(unittest.TestCase):
    def test_canonical_two_candidate_board(self):
        unrelated = {**BASE, "scope": "other"}
        broken = {**BASE, "key": "candidate:VF-OTHER-01"}
        results = parse_candidates([BASE, SECOND, unrelated, broken])
        self.assertEqual([x["id"] for x in results], ["VF-TEST-02", "VF-DEMO-01"])
        self.assertEqual(summary(results), {
            "total": 2, "in_discovery": 2,
            "pending_experiments": 1, "validation_claims": 0,
        })

    def test_no_false_market_validation(self):
        reported = {**BASE, "value": {**BASE["value"], "business_validated": True}}
        self.assertEqual(summary(parse_candidates([reported]))["validation_claims"], 1)

    def test_reject_duplicate_id(self):
        with self.assertRaisesRegex(WorkspaceError, "Duplicate"):
            parse_candidates([BASE, BASE])

    def test_reject_wrong_shapes(self):
        for value in (
            {**BASE["value"], "name": {"text": "invalid"}},
            {**BASE["value"], "stage": None},
            {**BASE["value"], "experiments": "planned"},
            {**BASE["value"], "hypotheses": "invalid"},
            {**BASE["value"], "metrics": "invalid"},
        ):
            with self.subTest(value=value), self.assertRaises(WorkspaceError):
                parse_candidates([{**BASE, "value": value}])

    def test_invalid_core_url(self):
        invalid = (
            "http://example.com", "ftp://example.com",
            "https://user:pass@core.example.com",
            "https://core.example.com/base",
            "https://core.example.com?key=secret",
            "https://core.example.com#fragment",
        )
        for address in invalid:
            with self.subTest(address=address), self.assertRaises(WorkspaceError):
                CoreStateStore(address, "testing-only-token")

    def test_core_get_only_scoped_and_bearer_server_side(self):
        store = CoreStateStore("https://internal.core.example", "testing-only-token")
        requests = []
        def fake_open(req, timeout=0):
            requests.append(req)
            return FakeResponse(json.dumps([BASE, SECOND]).encode("utf-8"))
        store._opener = Mock(open=fake_open)
        items = store.list_candidates()
        self.assertEqual(len(items), 2)
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].get_method(), "GET")
        self.assertEqual(requests[0].full_url, "https://internal.core.example" + ENDPOINT)
        self.assertEqual(requests[0].get_header("Authorization"), "Bearer testing-only-token")
        self.assertNotIn("testing-only-token", repr(items))
        self.assertNotIn("testing-only-token", requests[0].full_url)

    def test_writes_unconditionally_disabled(self):
        store = CoreStateStore("https://internal.core.example", "test-token")
        store._opener = Mock(open=Mock(side_effect=AssertionError("Network must not be reached")))
        with self.assertRaisesRegex(WorkspaceError, "disabled"):
            store.update_candidate("VF-DEMO-01", "old", {"notes": "new"})
        store._opener.open.assert_not_called()

    def test_invalid_http_response_and_size_limit(self):
        store = CoreStateStore("https://internal.core.example", "test-token")
        for raw in (b"not JSON", b"{}", b"[" + b"x" * MAX_RESPONSE_BYTES + b"]"):
            store._opener = Mock(open=lambda req, timeout=0: FakeResponse(raw))
            with self.subTest(size=len(raw)), self.assertRaises(WorkspaceError):
                store.list_candidates()

    def test_error_never_exposes_bearer(self):
        store = CoreStateStore("https://internal.core.example", "SECRET-TOKEN-NEVER-LOG")
        store._opener = Mock(open=Mock(side_effect=URLError("some internal transport error")))
        with self.assertRaises(WorkspaceError) as cm:
            store.list_candidates()
        self.assertNotIn("SECRET-TOKEN-NEVER-LOG", str(cm.exception))
        self.assertNotIn("internal transport error", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
