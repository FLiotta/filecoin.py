from filecoinpy.rpc.wallet import WalletRPC
from filecoinpy.rpc.i import IRPC
from filecoinpy.rpc.log import LogRPC

class FilecoinLotusRPC:
  def __init__(self, provider: str, token: str):
    self.wallet = WalletRPC(provider, token)
    self.i = IRPC(provider, token)
    self.log = LogRPC(provider, token)
