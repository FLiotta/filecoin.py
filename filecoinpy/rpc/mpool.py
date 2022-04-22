from typing import Optional, List
from filecoinpy.rpc.client import ClientRPC
import filecoinpy.rpc.types as rpc_types

class MpoolRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def mpool_get_nonce(self, address: str) -> int:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#mpoolgetnonce
    return self.rpc.call("Filecoin.MpoolGetNonce", [address])

  def mpool_pending(self, cids: Optional[List[dict]] = None) -> List[rpc_types.SignedMessageCID]:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#mpoolpending
    return self.rpc.call("Filecoin.MpoolPending", [cids])

  def mpool_push(self, message: rpc_types.SignedMessage) -> dict:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#mpoolpush
    return self.rpc.call("Filecoin.MpoolPush", [message])

  def mpool_push_message(self, message: rpc_types.SignedMessage, max_fee: Optional[str] = "0") -> rpc_types.SignedMessageCID:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#mpoolpushmessage
    return self.rpc.call("Filecoin.MpoolPushMessage", [message, max_fee])

  def mpool_push_untrusted(self, message: rpc_types.SignedMessageCID) -> dict:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.MpoolPushUntrusted", [message])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])

  def mpool_batch_push(self) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#closing
    return self.rpc.call("Filecoin.Closing", [])