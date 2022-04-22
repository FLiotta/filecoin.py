from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

@dataclass
class PrivateKey:
  Type: str
  PrivateKey: str

@dataclass
class AddressTypes(Enum):
  "bls"
  "secp256k1"
  "secp256k1-ledger"

@dataclass
class Signature:
  Type: int
  Data: str

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
class SignedMessage:
  Message: Message
  Signature: Signature
  
@dataclass
class SignedMessageCID:
  Message: Message
  Signature: Signature
  CID: dict

@dataclass
class DiscoverResponse:
  info: dict
  methods: List[any]
  openrpc: str

@dataclass
class VersionResponse:
  Version: str
  APIVersion: str
  BlockDelay: int