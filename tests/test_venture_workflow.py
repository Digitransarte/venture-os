"""Venture Discovery workflow: triage → record draft → Project Agent packet → CAS."""
import json
import unittest
from pathlib import Path
from copy import deepcopy

from venture_integration import VentureRecordError, fingerprint
from venture_integration.workflow import (
    prepare_promotion, prepare_project_agent_packet,
    prepare_discovery_workflow, persist_candidate_after_review,
)

FIXTURE = Path(__file__).resolve().parents[1] / "docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json"


class FakeAdapter:
    def __init__(self, project_slug="designeo"):
        self.project_slug = project_slug
        self.calls = []

    def append_atomic(self, record, **kwargs):
        self.calls.append((deepcopy(record), kwargs))
        return {"status": "created", "revision": 1, "digest": fingerprint(record),
                "record": record, "memory_id": "test-memory"}


class DiscoveryWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.opportunities = json.loads(FIXTURE.read_text(encoding="utf-8"))["opportunities"]

    def test_all_three_domains_produce_safe_candidate_and_specialist_packet(self):
        expected_agents = ["design-agent-v3", "illustration-agent", "consulting-agent"]
        for opportunity, agent in zip(self.opportunities, expected_agents):
            with self.subTest(opportunity=opportunity["title"]):
                before = deepcopy(opportunity)
                prepared = prepare_discovery_workflow(opportunity, project_slug="designeo")
                self.assertEqual(opportunity, before)
                self.assertEqual(prepared["status"], "prepared_not_persisted")
                self.assertFalse(prepared["external_action_authorized"])
                self.assertFalse(prepared["write_authorized"])
                record = prepared["venture_record"]
                packet = prepared["handoff"]
                self.assertEqual(record["core_project_slug"], "designeo")
                self.assertEqual(record["venture_ref"], opportunity["opportunity_ref"])
                self.assertEqual(record["stage"], "exploring")
                self.assertEqual(record["gate"]["status"], "pending")
                self.assertEqual(record["experiment"]["status"], "not_authorized")
                self.assertIsNone(record["economics"]["revenue"])
                self.assertIsNone(record["economics"]["contribution_margin"])
                self.assertFalse(record["economics"]["profitability_confirmed"])
                self.assertEqual(packet["from_agent"], "project-agent")
                self.assertEqual(packet["to_agent"], agent)
                self.assertEqual(packet["status"], "prepared_not_executed")
                self.assertEqual(packet["inputs"][0]["source_record_hash"],
                                 fingerprint(record))
                self.assertFalse(packet["decisions"][0]["authorizing_external_actions"])

    def test_observations_never_promoted_to_verified_market_evidence(self):
        record = prepare_promotion(self.opportunities[1], project_slug="designeo")
        self.assertEqual(len(record["evidence"]), 3)
        self.assertTrue(all(not e["independent_market_validation"] for e in record["evidence"]))
        self.assertEqual(record["evidence"][0]["classification"], "reported_observation")
        self.assertEqual(record["evidence"][2]["classification"], "unknown")
        self.assertTrue(all(e["verification_state"] == "unverified_report"
                            for e in record["evidence"]))

    def test_invalid_reference_or_destination_denied(self):
        src = deepcopy(self.opportunities[0])
        src["opportunity_ref"] = "../../other-project"
        with self.assertRaises(VentureRecordError):
            prepare_promotion(src, project_slug="designeo")
        with self.assertRaises(VentureRecordError):
            prepare_promotion(self.opportunities[0], project_slug="../other")

    def test_candidate_requires_explicit_consent_to_persist(self):
        adapter = FakeAdapter()
        prepared = prepare_discovery_workflow(self.opportunities[0], project_slug="designeo")
        with self.assertRaises(VentureRecordError):
            persist_candidate_after_review(prepared, adapter=adapter,
                                           expected_revision=0, expected_digest=None)
        self.assertEqual(adapter.calls, [])
        out = persist_candidate_after_review(
            prepared, adapter=adapter, expected_revision=0,
            expected_digest=None, authorized_internal_write=True)
        self.assertEqual(out["revision"], 1)
        self.assertEqual(len(adapter.calls), 1)
        self.assertEqual(adapter.calls[0][1]["expected_revision"], 0)
        self.assertIsNone(adapter.calls[0][1]["expected_digest"])

    def test_cross_project_mismatch_rejected_before_write(self):
        adapter = FakeAdapter("noetic-ink")
        prepared = prepare_discovery_workflow(self.opportunities[1], project_slug="designeo")
        with self.assertRaises(VentureRecordError):
            persist_candidate_after_review(
                prepared, adapter=adapter, expected_revision=0, expected_digest=None,
                authorized_internal_write=True)
        self.assertEqual(adapter.calls, [])

    def test_approval_claims_rejected_before_write(self):
        adapter = FakeAdapter()
        prepared = prepare_discovery_workflow(self.opportunities[1], project_slug="designeo")
        prepared["venture_record"]["gate"]["status"] = "approved"
        with self.assertRaises(VentureRecordError):
            persist_candidate_after_review(prepared, adapter=adapter,
                                           expected_revision=0, expected_digest=None,
                                           authorized_internal_write=True)
        self.assertEqual(adapter.calls, [])

    def test_unknown_domain_requires_manual_handoff_routing(self):
        src = deepcopy(self.opportunities[0])
        src["vertical"] = "other"
        record = prepare_promotion(src, project_slug="designeo")
        with self.assertRaises(VentureRecordError):
            prepare_project_agent_packet(record)

    def test_economics_stay_scenarios_and_dont_infer_sale(self):
        op = deepcopy(self.opportunities[0])
        op["economics"] = {
            "sale_price": "200.00", "materials_and_fulfilment": "15.00",
            "platform_fees": "15.00", "acquisition_cost": "30.00",
            "agent_cost": "5.00", "human_labour_cost": "45.00",
        }
        rec = prepare_promotion(op, project_slug="designeo")
        self.assertIsNone(rec["economics"]["revenue"])
        self.assertIsNone(rec["economics"]["contribution_margin"])
        self.assertEqual(rec["economics"]["assumption_scenario"]
                         ["contribution_after_variable_and_human_costs"], "90.00")
        self.assertFalse(rec["economics"]["profitability_confirmed"])


if __name__ == "__main__":
    unittest.main()
