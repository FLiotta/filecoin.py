from filecoinpy.rpc.client import ClientRPC

class IRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def ID(self) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#id
    return self.rpc.call("Filecoin.ID", [])
