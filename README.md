# filecoin.py

Python package with some utils to sign a filecoin message; for a fully working implementation check the `/examples` folder.

## How to sign a message
```py
from filecoinpy.sign import offline_sign_message
from filecoinpy.types import Message, SignedMessage

address: str = "..."
address_xprv: bytes = "..."

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

# Sign it
signed_message: SignedMessage = offline_sign_message(msg, address_xprv)
```

## Tests
```sh
$ python -m pytest
````
