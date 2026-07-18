import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "docs" / "_source_word"
CONVERTED_DIR = ROOT / "docs" / "_converted"
INVENTORY = ROOT / "docs" / "document-inventory.md"
METADATA = ROOT / "docs" / "_conversion-metadata.json"


def _metadata_by_source():
    return {item["source"]: item for item in json.loads(METADATA.read_text(encoding="utf-8"))}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class DocumentConversionTests(unittest.TestCase):
    def test_all_word_files_are_inventoried(self):
        inventory = INVENTORY.read_text(encoding="utf-8")
        sources = sorted(SOURCE_DIR.rglob("*.docx"))
        self.assertTrue(sources)
        self.assertEqual(set(_metadata_by_source()), {path.name for path in sources})
        for source in sources:
            self.assertIn(f"`{source.name}`", inventory)

    def test_each_word_file_has_corresponding_markdown(self):
        metadata = _metadata_by_source()
        for source in SOURCE_DIR.rglob("*.docx"):
            output = CONVERTED_DIR / metadata[source.name]["output"]
            self.assertTrue(output.is_file(), f"Markdown em falta para {source.name}")
            self.assertGreater(output.stat().st_size, 0)
            self.assertRegex(output.name, r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

    def test_original_word_files_have_not_changed(self):
        metadata = _metadata_by_source()
        for source in SOURCE_DIR.rglob("*.docx"):
            self.assertEqual(_sha256(source), metadata[source.name]["sha256"], source.name)


if __name__ == "__main__":
    unittest.main()
