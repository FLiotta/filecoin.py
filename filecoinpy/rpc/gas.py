from typing import Optional, List
from filecoinpy.rpc.client import ClientRPC
import filecoinpy.rpc.types as rpc_types

class GasRPC:
  def __init__(self, provider: str, token: str):
    self.rpc = ClientRPC(provider, token)

  def gas_estimate_fee_cap(self, message: rpc_types.Message, cids: Optional[List[dict]]) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#gasestimatefeecap
    if cids is not None:
      payload = [message, cids]
    else:
      payload = [message]

    return self.rpc.call("Filecoin.GasEstimateFeeCap", payload)
  
  def gas_estimate_gas_limit(self, message: rpc_types.Message, cids: Optional[List[dict]]) -> int:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#gasestimategaslimit
    if cids is not None:
      payload = [message, cids]
    else:
      payload = [message]

    return self.rpc.call("Filecoin.GasEstimateGasLimit", payload)
  
  def gas_estimate_gas_premium(
    self, 
    version: int, 
    address: str, 
    gas_limit: int, 
    cids: Optional[List[dict]]
  ) -> str:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#gasestimategaspremium
    return self.rpc.call("Filecoin.GasEstimateGasPremium", [version, address, gas_limit, cids])
  
  def gas_estimate_fee_cap(
    self, 
    message: rpc_types.Message, 
    cids: Optional[List[dict]],
    max_fee: Optional[str] = "0", 
  ) -> rpc_types.Message:
    # https://lotus.filecoin.io/developers/apis/json-rpc/#gasestimatemessagegas
    if cids is not None:
      payload = [message, max_fee, cids]
    else:
      payload = [message, max_fee]

    return self.rpc.call("Filecoin.GasEstimateMessageGas", payload)
