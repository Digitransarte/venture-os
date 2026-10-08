"""Pure, network-free migration tests."""
import json
import unittest
from copy import deepcopy
from pathlib import Path

from venture_integration import VentureRecordError, fingerprint
from venture_integration.migration import prepare_project_migration

FIXTURE = Path(__file__).resolve().parents[1] / "docs/integration/fixtures/VOS-PILOT-2026-001.json"


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.original = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_preserves_source_and_creates_distinct_destination_record(self):
        before = deepcopy(self.original)
        migrated = prepare_project_migration(
            self.original, destination_project_slug="noetic-ink",
            source_core_memory_id="5330aff8-1b83-4360-aa63-7b5d77f75bf5",
        )
        self.assertEqual(self.original, before)
        self.assertEqual(migrated["venture_ref"], before["venture_ref"])
        self.assertEqual(migrated["core_project_slug"], "noetic-ink")
        self.assertEqual(migrated["stage"], "exploring")
        self.assertEqual(migrated["gate"], before["gate"])
        self.assertEqual(migrated["experiment"], before["experiment"])
        self.assertEqual(migrated["migration_provenance"]["source_project_slug"], "designeo")
        self.assertEqual(migrated["migration_provenance"]["source_digest"], fingerprint(before))
        self.assertTrue(migrated["migration_provenance"]["historical_source_preserved"])
        self.assertFalse(migrated["migration_provenance"]["ceo_authorization_inferred"])

    def test_rejects_missing_source_and_same_project(self):
        for kw in (
            {"destination_project_slug": "designeo", "source_core_memory_id": "memo"},
            {"destination_project_slug": "noetic-ink", "source_core_memory_id": ""},
        ):
            with self.assertRaises(VentureRecordError):
                prepare_project_migration(self.original, **kw)

    def test_rejects_claimed_launch_and_approval(self):
        invalid = deepcopy(self.original)
        invalid["stage"] = "operating"
        with self.assertRaises(VentureRecordError):
            prepare_project_migration(invalid, destination_project_slug="noetic-ink",
                                      source_core_memory_id="src")
        invalid = deepcopy(self.original)
        invalid["gate"]["status"] = "approved"
        with self.assertRaises(VentureRecordError):
            prepare_project_migration(invalid, destination_project_slug="noetic-ink",
                                      source_core_memory_id="src")

    def test_rejects_repeat_migration_without_manual_review(self):
        migrated = prepare_project_migration(self.original,
                                             destination_project_slug="noetic-ink",
                                             source_core_memory_id="src")
        with self.assertRaises(VentureRecordError):
            prepare_project_migration(migrated,
                                      destination_project_slug="another-company",
                                      source_core_memory_id="src2")


if __name__ == "__main__":
    unittest.main()
