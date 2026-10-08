"""Opportunity radar: business facts, unknowns and economics must not be conflated."""
import json
import unittest
from copy import deepcopy
from pathlib import Path

from venture_integration import VentureRecordError
from venture_integration.discovery import (
    compare_briefs, opportunity_brief, unit_economics_preview,
)

RADAR = Path(__file__).resolve().parents[1] / "docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json"


class VentureDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(RADAR.read_text(encoding="utf-8"))["opportunities"]

    def test_three_live_domains_not_ranked_as_validated(self):
        briefs = compare_briefs(self.data)
        self.assertEqual(
            [x["vertical"] for x in briefs],
            ["design-web", "print-apparel", "metal-fabrication"]
        )
        self.assertEqual(len({x["opportunity_ref"] for x in briefs}), 3)
        for b in briefs:
            self.assertEqual(b["stage"], "discovery_not_validated")
            self.assertFalse(b["decision_gate"]["launch_recommended"])
            self.assertFalse(b["decision_gate"]["authorized_to_contact_or_publish"])
            self.assertEqual(b["reported_buyer_behaviour_or_sales"], 0)
            self.assertIsNone(b["unit_economics"]["contribution_after_variable_and_human_costs"])
            self.assertTrue(b["unknowns"])

    def test_noetic_missing_buyer_and_market_proof_explicit(self):
        b = opportunity_brief(self.data[1])
        self.assertIsNone(b["buyer_hypothesis"])
        self.assertIsNone(b["channel_hypothesis"])
        self.assertIn("Define a specific potential buyer", b["unknowns"])
        self.assertIn("No customer behaviour or paid transactions evidenced", b["unknowns"])
        self.assertEqual(b["evidence_counts"]["owner_observation"], 2)

    def test_source_is_required_for_observations_or_sales(self):
        c = deepcopy(self.data[0])
        c["evidence"].append({"type": "paid_transaction", "claim": "ten paid purchases"})
        with self.assertRaises(VentureRecordError):
            opportunity_brief(c)
        c["evidence"][-1]["source_ref"] = "transaction-ref-placeholder"
        b = opportunity_brief(c)
        self.assertEqual(b["reported_buyer_behaviour_or_sales"], 1)
        self.assertFalse(b["decision_gate"]["launch_recommended"])
        self.assertIn("sources still require independent checking", b["quality_flags"][1])

    def test_contradictory_evidence_is_not_discarded(self):
        c = deepcopy(self.data[0])
        c["evidence"].append({"type": "contradictory", "claim": "potential buyer declines",
                              "source_ref": "interview-1"})
        b = opportunity_brief(c)
        self.assertEqual(b["evidence_counts"]["contradictory"], 1)
        self.assertIn("Review contradictory evidence before selecting a test", b["unknowns"])

    def test_economic_preview_is_a_scenario_not_confirmed_profit(self):
        scenario = {
            "sale_price": "35.00",
            "materials_and_fulfilment": "9.50",
            "platform_fees": "2.20",
            "acquisition_cost": "7.00",
            "agent_cost": "0.30",
            "human_labour_cost": "8.00",
        }
        report = unit_economics_preview(scenario)
        self.assertEqual(report["contribution_after_variable_and_human_costs"], "8.00")
        self.assertFalse(report["profitability_confirmed"])
        self.assertEqual(report["input_status"], "complete_assumption_scenario")

    def test_missing_acquisition_or_human_cost_blocks_margin(self):
        preview = unit_economics_preview({
            "sale_price": "35",
            "materials_and_fulfilment": "9.5",
            "platform_fees": "2.2",
            "acquisition_cost": None,
            "agent_cost": "0.3",
            "human_labour_cost": None,
        })
        self.assertEqual(preview["input_status"], "incomplete")
        self.assertIsNone(preview["contribution_after_variable_and_human_costs"])
        self.assertIn("acquisition_cost", preview["missing_fields"])
        self.assertIn("human_labour_cost", preview["missing_fields"])

    def test_bad_costs_denied_not_silently_rounded(self):
        for value in (True, "-1.00", "NaN", "Infinity", "9.999", {}):
            with self.subTest(value=value), self.assertRaises(VentureRecordError):
                unit_economics_preview({"sale_price": value})
    
    def test_invalid_evidence_and_duplicate_ref_denied(self):
        c = deepcopy(self.data[0])
        c["evidence"] = [{"type": "fact", "claim": "invalid"}]
        with self.assertRaises(VentureRecordError):
            opportunity_brief(c)
        with self.assertRaises(VentureRecordError):
            compare_briefs([self.data[0], deepcopy(self.data[0])])

    def test_source_data_unchanged(self):
        before = deepcopy(self.data)
        compare_briefs(self.data)
        self.assertEqual(before, self.data)


if __name__ == "__main__":
    unittest.main()
