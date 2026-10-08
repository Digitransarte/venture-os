"""Contract-only tests. All Core I/O uses a fake in-memory boundary."""
import json
import unittest
from copy import deepcopy
from pathlib import Path

from venture_integration import (
    VentureRecordError, VentureCoreJournal, extract_snapshots,
    fingerprint, prepare_handoff, validate, KIND,
)

FIXTURE = Path(__file__).resolve().parents[1] / "docs/integration/fixtures/VOS-PILOT-2026-001.json"


class FakeCore:
    def __init__(self):
        self.memory = []

    def list_memory(self, kind, ref):
        return list(self.memory)

    def add_memory(self, entry):
        response = dict(entry)
        response["id"] = f"local-test-{len(self.memory)+1}"
        self.memory.append(response)
        return response


class VentureIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_legacy_non_atomic_adapter_fails_closed_by_default(self):
        fake = FakeCore()
        journal = VentureCoreJournal(fake.list_memory, fake.add_memory)
        with self.assertRaises(VentureRecordError):
            journal.append(self.record)
        self.assertEqual(len(fake.memory), 0)

    def test_fixture_has_real_uncertainty_and_correct_state(self):
        x = validate(self.record)
        self.assertEqual(x["stage"], "exploring")
        self.assertIsNone(x["economics"]["revenue"])
        self.assertIsNone(x["economics"]["contribution_margin"])
        self.assertFalse(x["experiment"]["launch_approved"])
        self.assertFalse(any(i.get("independent_market_validation") for i in x["evidence"]))

    def test_validation_does_not_change_source(self):
        source = deepcopy(self.record)
        validate(self.record)
        self.assertEqual(self.record, source)

    def test_missing_evidence_source_for_claim_of_validation_rejected(self):
        x = deepcopy(self.record)
        x["evidence"].append({"classification": "economic", "claim": "Paid orders",
                               "independent_market_validation": True})
        with self.assertRaises(VentureRecordError):
            validate(x)

    def test_premature_operating_stage_rejected(self):
        x = deepcopy(self.record)
        x["stage"] = "operating"
        with self.assertRaises(VentureRecordError):
            validate(x)

    def test_gate_alone_not_enough_without_launch_authorization(self):
        x = deepcopy(self.record)
        x["stage"] = "launching"
        x["gate"]["status"] = "approved"
        with self.assertRaises(VentureRecordError):
            validate(x)

    def test_prepared_handoff_is_not_execution(self):
        packet = prepare_handoff(self.record, "screenprint-os", "verified per-SKU costs")
        self.assertEqual(packet["status"], "prepared_not_executed")
        self.assertFalse(packet["external_action_authorized"])
        self.assertEqual(packet["source_record_hash"], fingerprint(self.record))
        with self.assertRaises(VentureRecordError):
            prepare_handoff(self.record, "some-unknown-agent", "do work")

    def test_snapshot_is_idempotent_and_append_only(self):
        fake = FakeCore()
        journal = VentureCoreJournal(fake.list_memory, fake.add_memory, single_writer_mode=True)
        one = journal.append(self.record)
        again = journal.append(self.record)
        self.assertEqual(one["status"], "created")
        self.assertEqual(one["revision"], 1)
        self.assertEqual(again["status"], "unchanged")
        self.assertEqual(len(fake.memory), 1)
        newer = deepcopy(self.record)
        newer["next_action"] = "Rever duas artes e confirmar a técnica."
        two = journal.append(newer)
        self.assertEqual(two["revision"], 2)
        self.assertEqual(len(fake.memory), 2)
        recovered = extract_snapshots(fake.memory, self.record["venture_ref"])
        self.assertEqual([s["revision"] for s in recovered], [1, 2])
        self.assertEqual(recovered[0]["record"]["next_action"], self.record["next_action"])

    def test_other_venture_does_not_change_our_revision(self):
        fake = FakeCore()
        fake.memory.append({
            "id": "other",
            "kind": KIND,
            "content": json.dumps({"revision": 7, "digest": "x",
                                   "record": {"venture_ref": "VOS-OTHER"}}),
        })
        journal = VentureCoreJournal(fake.list_memory, fake.add_memory, single_writer_mode=True)
        self.assertEqual(journal.append(self.record)["revision"], 1)

    def test_divergent_revisions_are_rejected(self):
        fake = FakeCore()
        journal = VentureCoreJournal(fake.list_memory, fake.add_memory, single_writer_mode=True)
        journal.append(self.record)
        variant = deepcopy(self.record)
        variant["next_action"] = "different"
        variant_digest = fingerprint(variant)
        fake.memory.append({
            "id": "conflict",
            "kind": KIND,
            "content": json.dumps({"revision": 1, "digest": variant_digest, "record": variant}),
        })
        with self.assertRaises(VentureRecordError):
            journal.append(self.record)

    def test_proof_of_core_confirmation_required(self):
        journal = VentureCoreJournal(lambda kind, ref: [], lambda entry: {}, single_writer_mode=True)
        with self.assertRaises(VentureRecordError):
            journal.append(self.record)


if __name__ == "__main__":
    unittest.main()
