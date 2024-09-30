# bitcoin-balance-api-python

Easy-to-use API for retrieving the balance of a Bitcoin wallet with https://bitcoin-balance-api.com/

Swagger: https://api-testnet.bitcoin-balance-api.com/docs/

## Get Balance

```
import requests
import json

address = "tb1qlw09ycnp3qgqw9alqgx93ed7cg5kmnyud326ky"

s = requests.Session()
r = s.get('https://api-testnet.bitcoin-balance-api.com/v1/address/%s' % (address))

if r.status_code == 200:
    response = json.loads(r.content)
    print(f'Bitcoin Balance: %s' % (response['balance']))

```
