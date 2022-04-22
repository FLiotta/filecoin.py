from filecoinpy.rpc.wallet import WalletRPC
from filecoinpy.rpc.i import IRPC
from filecoinpy.rpc.log import LogRPC
from filecoinpy.rpc.miscellaneous import MiscellaneousRPC
from filecoinpy.rpc.gas import GasRPC
from filecoinpy.rpc.mpool import MpoolRPC

class FilecoinLotusRPC:
  def __init__(self, provider: str, token: str):
    self.wallet = WalletRPC(provider, token)
    self.i = IRPC(provider, token)
    self.log = LogRPC(provider, token)
    self.miscellaneous = MiscellaneousRPC(provider, token)
    self.gas = GasRPC(provider, token)
    self.mpool = MpoolRPC(provider, token)
