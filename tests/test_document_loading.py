import re
import unittest
from pathlib import Path

from test_document_library import ROOT, parse_manifest


CONFIG = ROOT / "config" / "document-loading.yaml"
COMMIT_FILE_LIST = ROOT / "docs" / "first-commit-files.md"
TABLE_DOCUMENTS = (
    ROOT / "docs/canonical/explorer/explorer-dashboard.md",
    ROOT / "docs/canonical/operations/common-agent-operating-model.md",
    ROOT / "docs/canonical/templates/venture-project-record.md",
    ROOT / "docs/canonical/templates/core-output-templates.md",
)


def parse_loading_policy():
    """Parse the small mapping/list YAML subset used by document-loading.yaml."""
    policy = {}
    root_key = None
    child_key = None
    for raw_line in CONFIG.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line:
            continue
        indent = len(line) - len(line.lstrip())
        value = line.strip()
        if indent == 0 and value.endswith(":"):
            root_key = value[:-1]
            child_key = None
            policy[root_key] = [] if root_key in {"always", "reference_only", "excluded"} else {}
        elif indent == 2 and value.startswith("- "):
            policy[root_key].append(value[2:])
        elif indent == 2 and ":" in value:
            child_key, inline = value.split(":", 1)
            policy[root_key][child_key] = []
            if inline.strip() not in {"", "[]"}:
                raise AssertionError(f"Valor YAML inesperado: {raw_line}")
        elif indent == 4 and value.startswith("- "):
            policy[root_key][child_key].append(value[2:])
        else:
            raise AssertionError(f"Linha YAML não suportada: {raw_line}")
    return policy


def global_loading_paths(policy):
    paths = set(policy["always"])
    for section in ("by_agent", "by_task", "by_mode"):
        for values in policy[section].values():
            paths.update(values)
    return paths


def table_blocks(path):
    blocks = []
    current = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("|"):
            current.append((number, line))
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def unescaped_pipe_count(line):
    return sum(character == "|" and (index == 0 or line[index - 1] != "\\") for index, character in enumerate(line))


class DocumentLoadingTests(unittest.TestCase):
    def test_root_instruction_file_has_exact_name(self):
        self.assertTrue((ROOT / "AGENTS.md").is_file())
        self.assertFalse((ROOT / "AGENTS.md.md").exists())

    def test_first_documentation_commit_scope_is_exact_and_exists(self):
        quote = "`"
        items = [
            line[3:-1]
            for line in COMMIT_FILE_LIST.read_text(encoding="utf-8").splitlines()
            if line.startswith(f"- {quote}") and line.endswith(quote)
        ]
        self.assertEqual(len(items), 91)
        self.assertEqual(len(items), len(set(items)))
        self.assertIn("docs/first-commit-files.md", items)
        self.assertNotIn("tests/__pycache__/", items)
        for item in items:
            self.assertTrue((ROOT / item).is_file(), item)

    def test_all_configured_paths_exist(self):
        policy = parse_loading_policy()
        paths = set(policy["always"] + policy["reference_only"] + policy["excluded"])
        for section in ("by_agent", "by_task", "by_mode", "project_specific"):
            for values in policy[section].values():
                paths.update(values)
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)

    def test_duplicate_and_superseded_documents_are_excluded_from_loading(self):
        policy = parse_loading_policy()
        manifest = parse_manifest()
        forbidden = {item["canonical_path"] for item in manifest if item["classification"] in {"duplicate", "superseded"}}
        self.assertEqual(forbidden, set(policy["excluded"]))
        self.assertTrue(forbidden.isdisjoint(global_loading_paths(policy)))
        for values in policy["project_specific"].values():
            self.assertTrue(forbidden.isdisjoint(values))

    def test_project_documents_are_not_loaded_globally(self):
        policy = parse_loading_policy()
        projects = {item["canonical_path"] for item in parse_manifest() if item["classification"] == "project-specific"}
        self.assertEqual(projects, set(policy["project_specific"]["VOS-EXP-001"]))
        self.assertTrue(projects.isdisjoint(global_loading_paths(policy)))
        self.assertTrue(projects.isdisjoint(policy["reference_only"]))

    def test_reference_documents_are_not_always_loaded(self):
        policy = parse_loading_policy()
        references = {item["canonical_path"] for item in parse_manifest() if item["classification"] == "reference"}
        self.assertEqual(references, set(policy["reference_only"]))
        self.assertTrue(references.isdisjoint(policy["always"]))

    def test_orchestrator_minimum_documents_are_defined(self):
        policy = parse_loading_policy()
        required = {
            "docs/canonical/system/v0-1-scope-and-completion-map.md",
            "docs/canonical/operations/agent-function-handbook.md",
            "docs/canonical/operations/venture-os-orchestrator.md",
            "docs/canonical/templates/venture-project-record.md",
        }
        self.assertEqual(required, set(policy["always"]))

    def test_explorer_protocol_activation_policy(self):
        policy = parse_loading_policy()
        general = "docs/canonical/explorer/explorer-protocol.md"
        validation = "docs/canonical/explorer/explorer-validation-protocol.md"
        self.assertIn(general, policy["by_agent"]["explorer"])
        self.assertNotIn(validation, policy["by_agent"]["explorer"])
        self.assertIn(validation, policy["by_task"]["validation"])
        self.assertIn(validation, policy["by_mode"]["standard"])
        self.assertIn(validation, policy["by_mode"]["deep"])

    def test_explorer_interview_and_evidence_documents_remain_agent_specific(self):
        explorer = parse_loading_policy()["by_agent"]["explorer"]
        self.assertIn("docs/canonical/explorer/interview-guide.md", explorer)
        self.assertIn("docs/canonical/explorer/evidence-register.md", explorer)

    def test_reviewed_markdown_tables_are_valid(self):
        expected_counts = {
            "explorer-dashboard.md": 26,
            "common-agent-operating-model.md": 15,
            "venture-project-record.md": 9,
            "core-output-templates.md": 17,
        }
        for path in TABLE_DOCUMENTS:
            blocks = table_blocks(path)
            self.assertEqual(len(blocks), expected_counts[path.name], path)
            for block in blocks:
                counts = [unescaped_pipe_count(line) for _, line in block]
                self.assertEqual(len(set(counts)), 1, f"Colunas inconsistentes em {path}:{block[0][0]}")
                self.assertGreaterEqual(len(block), 2, f"Tabela incompleta em {path}:{block[0][0]}")
                separator_cells = block[1][1].strip("|").split("|")
                self.assertTrue(
                    all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell) for cell in separator_cells),
                    f"Separador inválido em {path}:{block[0][0]}",
                )


if __name__ == "__main__":
    unittest.main()
