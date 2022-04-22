from filecoinpy.rpc import FilecoinLotusRPC

provider = "your node entry point"
token = "your token"

client = FilecoinLotusRPC(provider, token)

address = client.wallet.wallet_new("secp256k1")

# ...
