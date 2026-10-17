"""Contract tests for SaaS feasibility calculations; all data hypothetical."""
import unittest

from venture_workspace.economics import Scenario, simulate


class SaaSEconomicsTests(unittest.TestCase):
    def test_zero_inputs_never_imply_revenue(self):
        result = simulate(Scenario())
        self.assertEqual(result["revenue_eur"], 0)
        self.assertEqual(result["operating_result_eur"], 0)
        self.assertIsNone(result["break_even_accounts"])
        self.assertTrue(result["estimate_only"])

    def test_tokens_fixed_support_and_payment(self):
        result = simulate(Scenario(
            paying_accounts=100, subscription_price_eur_ex_vat=10,
            ai_calls_per_account=20, input_tokens_per_call=1000,
            output_tokens_per_call=500, input_eur_per_million_tokens=2,
            output_eur_per_million_tokens=8,
            other_ai_tools_eur_per_account=0.5,
            storage_eur_per_account=0.2, support_minutes_per_account=3,
            support_hourly_eur=12, payment_percent=2,
            payment_fixed_eur_per_account=0.1,
            monthly_hosting_eur=50, monthly_backup_monitoring_eur=20,
            monthly_other_fixed_eur=30,
        ))
        # 20 * (1000*2 + 500*8)/1M = 0.12
        self.assertAlmostEqual(result["ai_tokens_eur_per_account"], 0.12)
        self.assertAlmostEqual(result["ai_eur_per_account"], 0.62)
        # AI .62 + storage .2 + support .6 + payment .3 = 1.72
        self.assertAlmostEqual(result["variable_eur_per_account"], 1.72)
        self.assertAlmostEqual(result["revenue_eur"], 1000)
        self.assertAlmostEqual(result["total_cost_eur"], 272)
        self.assertAlmostEqual(result["operating_result_eur"], 728)
        self.assertEqual(result["break_even_accounts"], 13)

    def test_nonviable_unit_economics_has_no_break_even(self):
        result = simulate(Scenario(paying_accounts=20,
                                   subscription_price_eur_ex_vat=1,
                                   storage_eur_per_account=2,
                                   monthly_hosting_eur=100))
        self.assertLess(result["operating_result_eur"], 0)
        self.assertIsNone(result["break_even_accounts"])

    def test_fixed_only_break_even(self):
        result = simulate(Scenario(subscription_price_eur_ex_vat=10,
                                   monthly_hosting_eur=99))
        self.assertEqual(result["break_even_accounts"], 10)

    def test_payment_and_counts_validated(self):
        for item in (
            Scenario(payment_percent=101),
            Scenario(monthly_hosting_eur=-0.1),
            Scenario(paying_accounts=-1),
            Scenario(ai_calls_per_account=1.5),
            Scenario(input_eur_per_million_tokens=float("nan")),
        ):
            with self.subTest(item=item), self.assertRaises(ValueError):
                simulate(item)


if __name__ == "__main__":
    unittest.main()
