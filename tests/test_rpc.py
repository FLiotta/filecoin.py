import requests

from unittest import TestCase
from unittest.mock import patch

from filecoinpy.rpc.client import ClientRPC, RPCError

def fake_rpc_call(*args, **kwargs):
  class FakeRPC:
    def json(self):
      return {"result": "ok"}
  
  return FakeRPC()

def fake_rpc_call_fail(*args, **kwargs):
  class FakeRPC:
    def json(self):
      return {
        "error": {
          "message": "F"
        }
      }
  
  return FakeRPC()

class TestUtils(TestCase):
  def setUp(self) -> None:
    self.rpc = ClientRPC("http://lol", "wqerx./qwer/wqxer.weqr")

  @patch.object(requests, "post", fake_rpc_call)
  def test_rpc(self):
    resp = self.rpc.call("Filecoin.Version", [])

    self.assertEqual(resp, "ok")

  @patch.object(requests, "post", fake_rpc_call_fail)
  def test_rpc_fail(self):
    with self.assertRaises(RPCError):
      self.rpc.call("Filecoin.Version", [])
