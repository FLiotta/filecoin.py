from typing import Optional
from dataclasses import dataclass

@dataclass
class Message:
  To: str
  From: str
  Nonce: int
  Value: str
  GasLimit: int
  Method: int
  GasFeeCap: Optional[str] = "0"
  GasPremium: Optional[str] = "0"
  Params: Optional[str] = ""

@dataclass
class Signature:
  Type: int
  Data: str

@dataclass
class SignedMessage:
  Message: Message
  Signature: Signature