#!/usr/bin/env python3
# script: retrieve bitcoin balance from bitcoin-balance-api.com
# author: Bitcoin Balance API <hello@bitcoin-balance-api.com>
# notes: 

import requests
import json

address = "tb1qlw09ycnp3qgqw9alqgx93ed7cg5kmnyud326ky"

s = requests.Session()
r = s.get('https://api-testnet.bitcoin-balance-api.com/v1/address/%s' % (address))

if r.status_code == 200:
    response = json.loads(r.content)
    print(f'Bitcoin Balance: %s' % (response['balance']))
