import base64
import secp256k1

from filecoinpy.types import Message, SignedMessage
from filecoinpy.utils import (
  CustomBlakeDigest,
  serialize_msg_to_cbor, 
  get_protocol_indicator_from_address,
  parse_hex_to_hex2
)

def offline_sign_message(msg: Message, xprv: bytes) -> SignedMessage:
  serialized_message = serialize_msg_to_cbor(msg)

  signing_key = secp256k1.PrivateKey(xprv)
  signature = signing_key.ecdsa_sign_recoverable(serialized_message, digest=CustomBlakeDigest)
  recover = signing_key.ecdsa_recoverable_serialize(signature)

  parsed_signature = base64.b64encode(
    bytes(recover[0]) + bytes.fromhex( parse_hex_to_hex2( hex(recover[1])[2:] ) )
  )

  return {
    "Message": msg,
    "Signature": {
      "Type": get_protocol_indicator_from_address(msg["From"]),
      "Data": parsed_signature.decode()
    }
  }

def offline_sign_bytes(bytes_: bytes, xprv: bytes) -> bytes:
  signing_key = secp256k1.PrivateKey(xprv)
  signature = signing_key.ecdsa_sign_recoverable(bytes_, digest=CustomBlakeDigest)
  recover = signing_key.ecdsa_recoverable_serialize(signature)

  parsed_signature = base64.b64encode(
    bytes(recover[0]) + bytes.fromhex( parse_hex_to_hex2( hex(recover[1])[2:] ) )
  )

  return parsed_signature
