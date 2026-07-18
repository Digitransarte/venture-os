import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = DOCS / "canonical-manifest.yaml"
CONVERTED = DOCS / "_converted"
SOURCE_WORD = DOCS / "_source_word"
SOURCE_HASHES = DOCS / "_conversion-metadata.json"
FRONT_MATTER_KEYS = {
    "title", "code", "version", "status", "document_role", "source_file",
    "supersedes", "superseded_by", "project",
}


def parse_manifest():
    """Parse the deliberately JSON-scalar YAML subset emitted by the builder."""
    documents = []
    current = None
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line == "documents:":
            continue
        if line.startswith("  - id: "):
            current = {"id": json.loads(line.removeprefix("  - id: "))}
            documents.append(current)
            continue
        if line.startswith("    ") and current is not None:
            key, value = line.strip().split(": ", 1)
            current[key] = json.loads(value)
    return documents


def parse_front_matter(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise AssertionError(f"Front matter em falta: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise AssertionError(f"Front matter não terminado: {path}") from error
    metadata = {}
    for line in lines[1:end]:
        key, value = line.split(": ", 1)
        metadata[key] = json.loads(value)
    body = "\n".join(lines[end + 1:]).lstrip("\n") + "\n"
    return metadata, body


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class DocumentLibraryTests(unittest.TestCase):
    def test_all_25_converted_documents_remain_present(self):
        self.assertEqual(len(list(CONVERTED.glob("*.md"))), 25)

    def test_word_originals_are_unchanged(self):
        recorded = {item["source"]: item["sha256"] for item in json.loads(SOURCE_HASHES.read_text(encoding="utf-8"))}
        sources = list(SOURCE_WORD.glob("*.docx"))
        self.assertEqual(len(sources), 25)
        for source in sources:
            self.assertEqual(sha256(source), recorded[source.name], source.name)

    def test_every_converted_document_has_one_manifest_classification(self):
        documents = parse_manifest()
        classified = [Path(item["source_markdown"]).name for item in documents]
        converted = [path.name for path in CONVERTED.glob("*.md")]
        self.assertEqual(len(documents), 25)
        self.assertEqual(len(classified), len(set(classified)))
        self.assertEqual(set(classified), set(converted))

    def test_all_manifest_paths_exist_and_preserve_source_body(self):
        for item in parse_manifest():
            classified = ROOT / item["canonical_path"]
            source = ROOT / item["source_markdown"]
            self.assertTrue(classified.is_file(), classified)
            self.assertTrue(source.is_file(), source)
            _, body = parse_front_matter(classified)
            self.assertEqual(body, source.read_text(encoding="utf-8"), classified)

    def test_no_two_canonical_documents_are_integrally_equivalent(self):
        hashes = {}
        for item in parse_manifest():
            if not item["canonical_path"].startswith("docs/canonical/"):
                continue
            _, body = parse_front_matter(ROOT / item["canonical_path"])
            digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
            self.assertNotIn(digest, hashes, f"Equivalentes: {hashes.get(digest)} e {item['id']}")
            hashes[digest] = item["id"]

    def test_all_canonical_documents_have_valid_yaml_metadata(self):
        allowed_statuses = {"Draft", "Candidate"}
        for item in parse_manifest():
            if not item["canonical_path"].startswith("docs/canonical/"):
                continue
            metadata, _ = parse_front_matter(ROOT / item["canonical_path"])
            self.assertEqual(set(metadata), FRONT_MATTER_KEYS)
            self.assertIn(metadata["status"], allowed_statuses)
            self.assertIn(item["classification"], {"canonical", "project-specific"})
            self.assertEqual(metadata["status"], item["status"])
            self.assertTrue(metadata["title"])
            self.assertTrue(metadata["document_role"])
            self.assertTrue(metadata["source_file"])


if __name__ == "__main__":
    unittest.main()
