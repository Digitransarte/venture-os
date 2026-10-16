"""Regression tests for the internal Venture Workspace data contract."""
import unittest

from venture_workspace.core_store import (
    CoreStateStore, WorkspaceError, parse_candidates, patch_candidate, summary,
)

BASE = {
    "scope": "venture-factory", "key": "candidate:VF-DEMO-01",
    "updated_at": "2026-10-16T10:00:00Z",
    "state_type": "venture_candidate", "provenance": "declared",
    "source": "test", "confidence": None,
    "value": {
        "schema": "designeo.venture.candidate.v0.1",
        "id": "VF-DEMO-01", "name": "Demo", "stage": "G0_discovery",
        "problem": "Initial hypothesis", "business_validated": False,
        "experiments": [{"name": "Interview", "status": "planned"}],
    },
}


class WorkspaceCoreTests(unittest.TestCase):
    def test_parsing_only_canonical_candidates(self):
        unrelated = {**BASE, "scope": "other"}
        broken = {**BASE, "key": "candidate:VF-OTHER-01"}
        results = parse_candidates([BASE, unrelated, broken])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "VF-DEMO-01")
        self.assertIn("_updated_at", results[0])

    def test_summary_does_not_claim_validation(self):
        result = summary(parse_candidates([BASE]))
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["in_discovery"], 1)
        self.assertEqual(result["pending_experiments"], 1)
        self.assertEqual(result["validated_businesses"], 0)

    def test_editor_preserves_state_and_original(self):
        original = parse_candidates([BASE])[0]
        updated = patch_candidate(original, {"problem": "New hypothesis"})
        self.assertEqual(updated["problem"], "New hypothesis")
        self.assertEqual(updated["stage"], "G0_discovery")
        self.assertFalse(updated["business_validated"])
        self.assertNotIn("_updated_at", updated)
        self.assertEqual(original["problem"], "Initial hypothesis")

    def test_editor_rejects_external_approvals(self):
        original = parse_candidates([BASE])[0]
        for forbidden in ("stage", "decision", "business_validated", "gate", "evidence", "id", "experiments"):
            with self.subTest(forbidden=forbidden), self.assertRaises(WorkspaceError):
                patch_candidate(original, {forbidden: "approved"})

    def test_editor_caps_user_content(self):
        with self.assertRaises(WorkspaceError):
            patch_candidate(BASE["value"], {"notes": "x" * 3001})

    def test_store_rejects_unsafe_base_url(self):
        for bad in ("http://example.com", "ftp://example.com", "https://user:pass@example.com", "https://example.com?a=b"):
            with self.subTest(url=bad), self.assertRaises(WorkspaceError):
                CoreStateStore(bad, "not-a-real-token")

    def test_default_write_locked(self):
        store = CoreStateStore("https://core.example.com", "mock")
        store._request = lambda *args: self.fail("Network should not be called")
        with self.assertRaisesRegex(WorkspaceError, "disabled"):
            store.update_candidate("VF-DEMO-01", BASE["updated_at"], {"notes": "x"})

    def test_optimistic_stale_version_refusal(self):
        store = CoreStateStore("https://core.example.com", "mock", allow_legacy_writes=True)
        calls = []
        def fake_request(method, path, body=None):
            calls.append(method)
            if method == "GET":
                return [BASE]
            self.fail("Must not PUT on stale revision")
        store._request = fake_request
        with self.assertRaisesRegex(WorkspaceError, "changed"):
            store.update_candidate("VF-DEMO-01", "stale", {"notes": "x"})
        self.assertEqual(calls, ["GET"])

    def test_allowed_update_sends_preserved_candidate_to_core(self):
        store = CoreStateStore("https://core.example.com", "mock", allow_legacy_writes=True)
        calls = []
        def fake_request(method, path, body=None):
            calls.append((method, path, body))
            if method == "GET":
                return [BASE]
            return {"value": body["value"], "updated_at": "next"}
        store._request = fake_request
        value = store.update_candidate("VF-DEMO-01", BASE["updated_at"], {"notes": "research"})
        self.assertEqual(value["value"]["notes"], "research")
        self.assertEqual(calls[1][0], "PUT")
        self.assertIn("candidate%3AVF-DEMO-01", calls[1][1])
        self.assertFalse(calls[1][2]["value"]["business_validated"])


if __name__ == "__main__":
    unittest.main()
