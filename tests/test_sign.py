from unittest import TestCase

from bip_utils import Bip44, Bip44Coins, Bip44Changes, Bip39SeedGenerator, Bip39MnemonicGenerator

from filecoinpy.sign import offline_sign_bytes, offline_sign_message
from filecoinpy.utils import serialize_msg_to_cbor
from filecoinpy.types import Message, SignedMessage

class TestUtils(TestCase):
  def setUp(self) -> None:
    mnemonic = " ".join(Bip39MnemonicGenerator().FromWordsNumber(12).m_mnemonic_list)
    seed = Bip39SeedGenerator(mnemonic).Generate()

    bip_mst_ctx = Bip44.FromSeed(seed, Bip44Coins.FILECOIN)
    bip_acc_ctx = bip_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)

    bip_address = bip_acc_ctx.AddressIndex(0)

    self.address = bip_address.PublicKey().ToAddress()
    self.address_xprv = bip_address.PrivateKey().Raw().ToBytes()

  def test_offline_sign_message(self):
    msg: Message = {
      "From": self.address,
      "To": "f1ysjje6bs74mnluhbc25sigsmaggjrknnn3f34fa",
      "Value": "150",
      "GasLimit": 295063,
      "GasFeeCap": "150000000000",
      "GasPremium": "150000000000",
      "Nonce": 0,
      "Method": 0,
      "Params": ""
    }
    
    signed_message: SignedMessage = offline_sign_message(msg, self.address_xprv)

    self.assertIsNotNone(signed_message)
    self.assertIn("Message", signed_message)
    self.assertIn("Signature", signed_message)

  def offline_sign_bytes(self):
    msg: Message = {
      "From": self.address,
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

    signature = offline_sign_bytes(serialized_msg, self.address_xprv)

    self.assertIsNotNone(signature)
    self.assertEqual(type(signature), bytes)