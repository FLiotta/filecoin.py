from typing import List

from filecoinpy.rpc.client import ClientRPC
import filecoinpy.rpc.types as rpc_types

class LogRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def log_alerts(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#logalerts
    return self.rpc.call("Filecoin.LogAlerts", [])

  def log_list(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#loglist
    return self.rpc.call("Filecoin.LogList", [])

  def log_set_level(self, payload: List[str]) -> dict:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#logsetlevel
    return self.rpc.call("Filecoin.LogSetLevel", [])
