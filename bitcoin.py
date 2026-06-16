import requests

import json

import sys
response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=2228f11c92d6b21490bd55aa584fa054294188c172abfee3791c613fc98b4ce2"
        )
try:
    if len(sys.argv) == 2:
        n = float(sys.argv[1])

    elif len(sys.argv) < 2:
        sys.exit("Missing Argument")

    elif len(sys.argv) > 2:
        sys.exit("Too many Agruments")

except ValueError:
        sys.exit("Enter a valid number")

    
price = response.json()
btc_price = float(price['data']["priceUsd"])

total = btc_price * n
print(f"1 bitcoin ${btc_price}\nPrice of {n} bitcoins is {total:,.4f}")


