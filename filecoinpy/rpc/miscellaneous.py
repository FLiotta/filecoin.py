from filecoinpy.rpc.client import ClientRPC
import filecoinpy.rpc.types as rpc_types

class MiscellaneousRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def closing(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def discover(self) -> rpc_types.DiscoverResponse:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#discover
    return self.rpc.call("Filecoin.Discover", [])

  def session(self) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#session
    return self.rpc.call("Filecoin.Session", [])
  
  def shutdown(self) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#shutdown
    return self.rpc.call("Filecoin.Shutdown", [])
  
  def version(self) -> rpc_types.VersionResponse:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#version
    return self.rpc.call("Filecoin.Version", [])
