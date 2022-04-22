import cbor2
import base64
import leb128
import hashlib

from filecoinpy.types import Message
from filecoinpy.constants import CID_PREFIX, PROTOCOL_INDICATORS
from filecoinpy.exceptions import (
  InvalidChecksum, 
  InvalidLength, 
  InvalidProtocol, 
)

def get_protocol_indicator_from_address(address: str):
  # https://spec.filecoin.io/appendix/address/#section-appendix.address.protocol-indicator

  return address[1]

def get_checksum(payload: bytes) -> str:
  blakectx = hashlib.blake2b(payload, digest_size=4)
  
  return blakectx.hexdigest()

def parse_hex_to_hex2(hex_: str) -> str:
  hex_needs_to_be_pair_up = len(hex_) % 2 == 1

  if hex_needs_to_be_pair_up:
      return hex_.zfill( len(hex_) + 1 )
  
  return hex_

def parse_address_to_bytes(address: str) -> bytes:
  # https://spec.filecoin.io/appendix/address/#section-appendix.address

  protocol_indicator = address[1]
  protocol_indicator_byte = parse_hex_to_hex2(
    hex(int(protocol_indicator))[2:] # We remove 0x...
  )

  if protocol_indicator == PROTOCOL_INDICATORS["SECP256K1"]:
      address_decoded = base64.b32decode(address[2:].upper() + "=") # Puede traer problema este padding a futuro?
      payload = address_decoded[0:-4]
      checksum = address_decoded[-4:]
      
      if len(payload) != 20:
          raise InvalidLength
  elif protocol_indicator == PROTOCOL_INDICATORS["ID"]:
      if len(address) > 18:
          raise InvalidLength
  
      return bytes.fromhex(protocol_indicator_byte) + leb128.u.encode(int(address[2:]))
  else:
      raise InvalidProtocol

  bytes_address = bytes.fromhex(protocol_indicator_byte) + payload
  
  if get_checksum(bytes_address) != checksum.hex():
      raise InvalidChecksum

  return bytes_address

def parse_bignum_to_bytes(number: str) -> bytes:
  value_as_int = int(number)

  if value_as_int == 0:
      return b""
  
  value_as_hex = hex(value_as_int)[2:]

  value_as_hex2 = parse_hex_to_hex2(value_as_hex)

  return bytes.fromhex("00" + value_as_hex2)

def serialize_msg_to_cbor(msg: Message) -> bytes:
  # https://spec.filecoin.io/systems/filecoin_files/serialization/
  msg_to_serialize = [
    0,
    parse_address_to_bytes(msg["To"]),
    parse_address_to_bytes(msg["From"]),
    msg["Nonce"],
    parse_bignum_to_bytes(msg["Value"]),
    msg["GasLimit"],
    parse_bignum_to_bytes(msg["GasFeeCap"]),
    parse_bignum_to_bytes(msg["GasPremium"]),
    msg["Method"],
    base64.b64encode(msg["Params"].encode())
  ]

  return cbor2.dumps(msg_to_serialize)

def digest_message_with_cid(msg: bytes) -> bytes:
  message_hashed = hashlib.blake2b(digest_size=32)
  message_hashed.update(msg)
  message_hashed = message_hashed.digest()

  cid_prefix = hashlib.blake2b(digest_size=32)
  cid_prefix.update(CID_PREFIX)
  cid_prefix.update(message_hashed)
  cid_prefix = cid_prefix.digest()

  return cid_prefix

class CustomBlakeDigest:
  def __init__(self, msg: bytes):
    self.msg: bytes = msg

  def digest(self) -> bytes:
    return digest_message_with_cid(self.msg)