import json
import unittest
from pathlib import Path
from unittest.mock import Mock
from urllib.error import HTTPError

from venture_integration.core_http import CoreMemoryHttpAdapter, CoreTransportError
from venture_integration import fingerprint


class Response:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self):
        return json.dumps(self.value).encode("utf-8")


class CoreHttpAdapterTests(unittest.TestCase):
    def make_adapter(self):
        return CoreMemoryHttpAdapter(
            base_url="https://os.designeo.pt", api_token="TEST_ONLY_SECRET",
            project_slug="designeo",
        )

    def test_https_required_nonloopback(self):
        with self.assertRaises(ValueError):
            CoreMemoryHttpAdapter(
                base_url="http://os.designeo.pt",
                api_token="test", project_slug="designeo",
            )
        with self.assertRaises(ValueError):
            CoreMemoryHttpAdapter(
                base_url="https://user:password@os.designeo.pt",
                api_token="test", project_slug="designeo",
            )
        with self.assertRaises(ValueError):
            CoreMemoryHttpAdapter(
                base_url="https://os.designeo.pt",
                api_token="", project_slug="designeo",
            )

    def test_read_uses_scoped_kind_and_ref(self):
        adapter = self.make_adapter()
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return Response([{"id": "m1", "kind": "venture_record_snapshot_v01",
                              "content": "{}"}])

        adapter._opener = Mock(open=opener)
        result = adapter.list_memory("venture_record_snapshot_v01", "VOS-PILOT-2026-001")
        self.assertEqual(result[0]["id"], "m1")
        self.assertIn("kind=venture_record_snapshot_v01", requests[0].full_url)
        self.assertIn("q=VOS-PILOT-2026-001", requests[0].full_url)
        self.assertEqual(requests[0].get_method(), "GET")
        self.assertEqual(requests[0].get_header("Authorization"), "Bearer TEST_ONLY_SECRET")

    def test_write_is_explicit_and_scoped_to_project(self):
        adapter = self.make_adapter()
        requests = []

        def opener(request, timeout):
            requests.append(request)
            return Response({"id": "new-id", "kind": "note"})

        adapter._opener = Mock(open=opener)
        result = adapter.add_memory({
            "title": "ordinary note", "kind": "note",
            "content": "test", "tags": ["venture-os"], "unexpected": "ignored"
        })
        self.assertEqual(result["id"], "new-id")
        request = requests[0]
        self.assertEqual(request.get_method(), "POST")
        self.assertTrue(request.full_url.endswith("/v1/projects/designeo/memory"))
        data = json.loads(request.data.decode("utf-8"))
        self.assertNotIn("unexpected", data)
        self.assertNotIn("TEST_ONLY_SECRET", request.data.decode("utf-8"))

    def test_unversioned_snapshot_write_is_blocked(self):
        adapter = self.make_adapter()
        adapter._opener = Mock(open=lambda request, timeout: self.fail("Network must not run"))
        with self.assertRaises(CoreTransportError):
            adapter.add_memory({"kind": "venture_record_snapshot_v01",
                                "content": "{}"})

    def test_atomic_append_scoped_and_verified(self):
        adapter = self.make_adapter()
        record = json.loads((Path(__file__).resolve().parents[1] /
                             "docs/integration/fixtures/VOS-PILOT-2026-001.json").read_text(encoding="utf-8"))
        calls = []

        def opener(request, timeout):
            calls.append(request)
            if request.get_method() == "GET":
                return Response({"revision": 1, "digest": fingerprint(record),
                                 "record": record, "memory_id": "m1"})
            payload = json.loads(request.data.decode("utf-8"))
            self.assertEqual(payload["expected_revision"], 0)
            self.assertIsNone(payload["expected_digest"])
            self.assertEqual(payload["record"]["venture_ref"], record["venture_ref"])
            return Response({"revision": 1, "digest": fingerprint(record),
                             "record": record, "memory_id": "m1", "status": "created"})

        adapter._opener = Mock(open=opener)
        result = adapter.append_atomic(record, expected_revision=0, expected_digest=None)
        self.assertEqual(result["revision"], 1)
        self.assertEqual(adapter.get_latest(record["venture_ref"])["revision"], 1)
        self.assertIn("/venture-records/", calls[0].full_url)
        self.assertTrue(calls[0].full_url.endswith("/revisions"))
        self.assertEqual(calls[0].get_method(), "POST")

    def test_atomic_cross_project_write_rejected_before_network(self):
        adapter = self.make_adapter()
        record = json.loads((Path(__file__).resolve().parents[1] /
                             "docs/integration/fixtures/VOS-PILOT-2026-001.json").read_text(encoding="utf-8"))
        record["core_project_slug"] = "another"
        adapter._opener = Mock(open=lambda request, timeout: self.fail("Network must not run"))
        with self.assertRaises(CoreTransportError):
            adapter.append_atomic(record, expected_revision=0, expected_digest=None)

    def test_missing_venture_returns_none_and_other_errors_not_hidden(self):
        adapter = self.make_adapter()
        def missing(request, timeout):
            raise HTTPError(request.full_url, 404, "not found", {}, None)
        adapter._opener = Mock(open=missing)
        self.assertIsNone(adapter.get_latest("VOS-PILOT-2026-001"))
        def not_allowed(request, timeout):
            raise HTTPError(request.full_url, 403, "forbidden", {}, None)
        adapter._opener = Mock(open=not_allowed)
        with self.assertRaises(CoreTransportError) as error:
            adapter.get_latest("VOS-PILOT-2026-001")
        self.assertEqual(error.exception.status_code, 403)

    def test_http_error_message_does_not_expose_token(self):
        adapter = self.make_adapter()
        def opener(request, timeout):
            raise HTTPError(request.full_url, 401, "bad auth", {}, None)
        adapter._opener = Mock(open=opener)
        with self.assertRaises(CoreTransportError) as err:
            adapter.get_project()
        self.assertIn("401", str(err.exception))
        self.assertNotIn("TEST_ONLY_SECRET", str(err.exception))

    def test_project_mismatch_detected(self):
        adapter = self.make_adapter()
        adapter._opener = Mock(open=lambda request, timeout: Response({"slug": "other"}))
        with self.assertRaises(CoreTransportError):
            adapter.get_project()


if __name__ == "__main__":
    unittest.main()
