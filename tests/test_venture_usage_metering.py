"""Privacy and accuracy tests for manual AI consumption summaries."""
import unittest
from venture_workspace.usage_metering import (
    COLUMNS, UsageError, parse_usage, read_aggregates_csv, totals,
)


def row(**changes):
    default = {
        "month": "2026-10", "app": "learning-os",
        "operation": "tutor_feedback", "provider": "openrouter",
        "model": "openai/gpt-4.1-mini", "requests": 10,
        "input_tokens": 2500, "output_tokens": 1200,
        "cost_eur": "0.15", "source_kind": "provider_dashboard",
    }
    return {**default, **changes}


class UsageTests(unittest.TestCase):
    def test_monthly_usage(self):
        result = parse_usage(row())
        self.assertEqual(result.requests, 10)
        self.assertEqual(result.operation, "tutor_feedback")
        self.assertEqual(result.as_json()["reconciled"], False)

    def test_no_pii_fields_can_be_imported(self):
        for private in ("student_id", "email", "prompt", "transcript", "session_id"):
            with self.subTest(private=private), self.assertRaises(UsageError):
                parse_usage(row(**{private: "private"}))

    def test_bad_tags_and_bad_values(self):
        for invalid in (
            {"model": "personal@example.com"},
            {"month": "2026-13"},
            {"requests": -1},
            {"input_tokens": "abc"},
            {"cost_eur": "-1"},
            {"cost_eur": "NaN"},
            {"source_kind": "verified"},
        ):
            with self.subTest(invalid=invalid), self.assertRaises(UsageError):
                parse_usage(row(**invalid))

    def test_invoice_without_cost_is_rejected(self):
        with self.assertRaises(UsageError):
            parse_usage(row(cost_eur="", source_kind="provider_invoice"))

    def test_aggregate_never_assumes_unknown_cost_is_zero(self):
        entries = [
            parse_usage(row()),
            parse_usage(row(operation="audio_transcription", cost_eur="", requests=5,
                            input_tokens=0, output_tokens=0)),
        ]
        report = totals(entries)
        self.assertEqual(report["requests"], 15)
        self.assertEqual(report["requests_with_cost"], 10)
        self.assertTrue(report["any_missing_cost"])
        self.assertFalse(report["reconciled_with_provider"])
        self.assertEqual(report["declared_cost_eur"], "0.15")
        self.assertAlmostEqual(report["coverage_percent"], 66.6666666, places=4)

    def test_csv_rejects_extra_columns_before_parsing(self):
        content = (",".join(COLUMNS) + ",name\n" + ",".join(
            ["2026-10", "learning-os", "card_generation", "openrouter",
             "model", "1", "1", "1", "0.1", "manual_estimate", "student"])).encode()
        with self.assertRaisesRegex(UsageError, "approved aggregate"):
            read_aggregates_csv(content)

    def test_csv_rows_and_bom(self):
        csv_text = ",".join(COLUMNS) + "\n2026-10,learning-os,card_generation,openrouter,model,4,140,280,,manual_estimate\n"
        data = read_aggregates_csv(("\ufeff" + csv_text).encode())
        self.assertEqual(len(data), 1)
        self.assertIsNone(data[0].cost_eur)

    def test_reject_oversized_input(self):
        with self.assertRaises(UsageError):
            read_aggregates_csv(b"x" * 128001)

    def test_no_rows_has_no_fake_coverage(self):
        value = totals([])
        self.assertIsNone(value["coverage_percent"])
        self.assertEqual(value["requests"], 0)


if __name__ == "__main__":
    unittest.main()
