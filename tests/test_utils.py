from unittest import TestCase

from filecoinpy.utils import (
  get_protocol_indicator_from_address,
  parse_bignum_to_bytes,
  parse_address_to_bytes,
  parse_hex_to_hex2,
  get_checksum,
  serialize_msg_to_cbor,
  digest_message_with_cid
)
from filecoinpy.constants import PROTOCOL_INDICATORS
from filecoinpy.exceptions import InvalidProtocol
from filecoinpy.types import Message

class TestUtils(TestCase):
  def test_get_protocol_indicator_from_address(self):
    # SECP256k1
    address = "f17uoq6tp427uzv7fztkbsnn64iwotfrristwpryy"

    protocol_indicator = get_protocol_indicator_from_address(address)

    self.assertIsNotNone(protocol_indicator)
    self.assertEqual(protocol_indicator, PROTOCOL_INDICATORS["SECP256K1"])

    # ID
    address = "f01729"

    protocol_indicator = get_protocol_indicator_from_address(address)

    self.assertIsNotNone(protocol_indicator)
    self.assertEqual(protocol_indicator, PROTOCOL_INDICATORS["ID"])

  def test_parse_address_to_bytes(self):
    # SECP256k1
    address = "f17uoq6tp427uzv7fztkbsnn64iwotfrristwpryy"

    address_bytes = parse_address_to_bytes(address)

    self.assertIsNotNone(address_bytes)
    self.assertEqual(type(address_bytes), bytes)

    # ID
    address = "f01729"

    address_bytes = parse_address_to_bytes(address)

    self.assertIsNotNone(address_bytes)
    self.assertEqual(type(address_bytes), bytes)

    # Unknown
    address = "f9julio1816argentina"

    with self.assertRaises(InvalidProtocol):
      parse_address_to_bytes(address)

  def test_parse_hex_to_hex2(self):
    hex_ = hex(10)[2:] # a

    self.assertEqual(len(hex_), 1)

    hex2 = parse_hex_to_hex2(hex_)

    self.assertEqual(len(hex2), 2)
    self.assertEqual(hex2, "0a")
  
  def test_get_checksum(self):
    payload = b"Hola mundo!"

    checksum = get_checksum(payload)

    self.assertEqual(type(checksum), str)
    self.assertEqual(len(checksum), 8)
  
  def test_parse_bignum_to_bytes(self):
    big_num = "1500000000000"

    parsed_big_num = parse_bignum_to_bytes(big_num)

    self.assertIsNotNone(parsed_big_num)
    self.assertEqual(type(parsed_big_num), bytes)
    self.assertEqual(parsed_big_num, b'\x00\x01]>\xf7\x98\x00')
  
  def test_serialize_msg_to_cbor(self):
    msg: Message = {
      "From": "f17uoq6tp427uzv7fztkbsnn64iwotfrristwpryy",
      "To": "f1ysjje6bs74mnluhbc25sigsmaggjrknnn3f34fa",
      "Value": "150",
      "GasLimit": 295063,
      "GasFeeCap": "150000000000",
      "GasPremium": "150000000000",
      "Nonce": 0,
      "Method": 0,
      "Params": ""
    }

    serialized_msg = serialize_msg_to_cbor(msg)

    self.assertIsNotNone(serialized_msg)
    self.assertEqual(type(serialized_msg), bytes)

  def test_digest_message_with_cid(self):
    msg: Message = {
      "From": "f17uoq6tp427uzv7fztkbsnn64iwotfrristwpryy",
      "To": "f1ysjje6bs74mnluhbc25sigsmaggjrknnn3f34fa",
      "Value": "150",
      "GasLimit": 295063,
      "GasFeeCap": "150000000000",
      "GasPremium": "150000000000",
      "Nonce": 0,
      "Method": 0,
      "Params": ""
    }

    serialized_msg = serialize_msg_to_cbor(msg)

    digested_msg = digest_message_with_cid(serialized_msg)

    self.assertIsNotNone(digested_msg)
    self.assertEqual(type(digested_msg), bytes)