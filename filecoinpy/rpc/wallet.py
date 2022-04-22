from typing import List

from filecoinpy.rpc.client import ClientRPC
import filecoinpy.rpc.types as rpc_types

class WalletRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def wallet_balance(self, address: str) -> int:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletbalance
    return self.rpc.call("Filecoin.WalletBalance", [address])

  def wallet_default_address(self) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletdefaultaddress
    return self.rpc.call("Filecoin.WalletDefaultAddress", [])

  def wallet_delete(self, address: str) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletdelete
    return self.rpc.call("Filecoin.WalletDelete", [address])
    
  def wallet_export(self, address: str) -> rpc_types.PrivateKey:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletexport
    return self.rpc.call("Filecoin.WalletExport", [address])

  def wallet_has(self, address: str) -> bool:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#wallethas
    return self.rpc.call("Filecoin.WalletHas", [address])

  def wallet_import(self, private_key: rpc_types.PrivateKey) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletimport
    return self.rpc.call("Filecoin.WalletImport", [private_key])

  def wallet_list(self) -> List[str]:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletlist
    return self.rpc.call("Filecoin.WalletList", [])
  
  def wallet_new(self, wallet_type: rpc_types.AddressTypes) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletnew
    return self.rpc.call("Filecoin.WalletNew", [wallet_type])
  
  def wallet_set_default(self, address: str) -> None:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletsetdefault
    return self.rpc.call("Filecoin.WalletNew", [address])

  def wallet_sign(self, address: str, bytes_: str) -> rpc_types.Signature:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletsign
    return self.rpc.call("Filecoin.WalletSign", [address, bytes_])
  
  def wallet_sign_message(self, address: str, message: rpc_types.Message) -> rpc_types.SignedMessageCID:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletsignmessage
    return self.rpc.call("Filecoin.WalletSignMessage", [address, message])
  
  def wallet_validate_address(self, address: str) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletvalidateaddress
    return self.rpc.call("Filecoin.WalletValidateAddress", [address])
  
  def wallet_verify(self, address: str, bytes_: str, signature: rpc_types.Signature) -> bool:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#walletverify
    return self.rpc.call("Filecoin.WalletValidateAddress", [address, bytes_, signature])
