# https://spec.filecoin.io/appendix/address/#section-appendix.address.protocol-indicator
PROTOCOL_INDICATORS = {
  "ID": "0",
  "SECP256K1": "1",
  "ACTOR": "2",
  "BLS": "3"
}

CID_PREFIX = bytearray([0x01, 0x71, 0xa0, 0xe4, 0x02, 0x20])