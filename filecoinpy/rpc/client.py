import requests

from typing import List

from filecoinpy.exceptions import RPCError

class ClientRPC:
  def __init__(self, provider: str, token: str):
      self.provider = provider
      self.token = token

  def call(self, method: str, params: List[any] = []) -> any:
    headers = {
      "Authorization": f"Bearer {self.token}"
    }
    payload = {
      "json": 2,
      "method": method,
      "params": params,
      "id": 3
    }

    resp = requests.post(
      self.provider,
      headers=headers,
      json=payload
    )

    resp_data = resp.json()

    if resp_data.get("error"):
      raise RPCError(
        resp_data.get("error", "Unknown Error").get(
          "message", "Unknown Error"
        )
      )
    
    if resp_data.get("result"):
      return resp_data["result"]
    
    return ""
