import logging
import json

from bip_utils import Bip44, Bip44Coins, Bip44Changes ,Bip39SeedGenerator, Bip39MnemonicGenerator

from filecoinpy.types import Message, SignedMessage
from filecoinpy.sign import offline_sign_message, offline_sign_bytes
from filecoinpy.utils import serialize_msg_to_cbor

logging.basicConfig(level=logging.INFO)

# 1- Derive an address (just for example purposes)(extra)
# 2- Define Message
# 3- Sign it


# We derive an address (This is an extra step, this is only to show the whole process from the beggining)
mnemonic = " ".join(Bip39MnemonicGenerator().FromWordsNumber(12).m_mnemonic_list)
print(mnemonic)
seed = Bip39SeedGenerator(mnemonic).Generate()

bip_mst_ctx = Bip44.FromSeed(seed, Bip44Coins.FILECOIN)
bip_acc_ctx = bip_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)

bip_address = bip_acc_ctx.AddressIndex(0)

address = bip_address.PublicKey().ToAddress()
address_xprv = bip_address.PrivateKey().Raw().ToBytes()

logging.info(f"address: {address}")
logging.info(f"address_xprv: {address_xprv}\n\n")

# Define message
msg: Message = {
  "From": address,
  "To": "f1ysjje6bs74mnluhbc25sigsmaggjrknnn3f34fa",
  "Value": "150",
  "GasLimit": 295063,
  "GasFeeCap": "150000000000",
  "GasPremium": "150000000000",
  "Nonce": 0,
  "Method": 0,
  "Params": ""
}

logging.info(f"message: {json.dumps(msg, indent=2)}\n\n")

# Sign it
logging.info(f"========SIGNING========")
signed_message: SignedMessage = offline_sign_message(msg, address_xprv)

logging.info(f"signed message: {json.dumps(signed_message, indent=2)}\n\n")

# or

# Sign it manually
logging.info(f"===SIGNING MANUALLY===")
msg_serialized = serialize_msg_to_cbor(msg)
signature = offline_sign_bytes(msg_serialized, address_xprv)

logging.info(f"msg serialized: {msg_serialized}")
logging.info(f"signature: {signature}")

signed_message = {
  "Message": msg,
  "Signature": {
    "Type": 1,
    "Data": signature.decode()
  }
}

logging.info(f"signed message: {json.dumps(signed_message, indent=2)}\n\n")