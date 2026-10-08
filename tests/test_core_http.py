import json
import unittest
from unittest.mock import Mock
from urllib.error import HTTPError

from venture_integration.core_http import CoreMemoryHttpAdapter, CoreTransportError


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
            return Response({"id": "new-id", "kind": "venture_record_snapshot_v01"})

        adapter._opener = Mock(open=opener)
        result = adapter.add_memory({
            "title": "rev001", "kind": "venture_record_snapshot_v01",
            "content": "test", "tags": ["venture-os"], "unexpected": "ignored"
        })
        self.assertEqual(result["id"], "new-id")
        request = requests[0]
        self.assertEqual(request.get_method(), "POST")
        self.assertTrue(request.full_url.endswith("/v1/projects/designeo/memory"))
        data = json.loads(request.data.decode("utf-8"))
        self.assertNotIn("unexpected", data)
        self.assertNotIn("TEST_ONLY_SECRET", request.data.decode("utf-8"))

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
