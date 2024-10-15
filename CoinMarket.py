# --API-- #
# 071c564a-f754-47e9-828c-1ec14149b80e

import requests

# Define the endpoint and headers
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# Define the endpoint and headers
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '071c564a-f754-47e9-828c-1ec14149b80e',
}

# Define los parámetros para la solicitud
parameters = {
  #'start':'1',
  #'limit':'5000',
  'symbol' :"BTC,ETH",
  'convert':'USD'  
}


# Realiza la solicitud para obtener el precio de Bitcoin
def get_btc_price():
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    try:
        price_btc = data['data']['BTC']['quote']['USD']['price']
        print(f"El precio actual de BTC es: ${price_btc:.2f}")
    except KeyError as e:
        print(e)

# Realiza la solicitud para obtener el precio de Ethereum
def get_eth_price():
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    try:
        price_eth = data['data']['ETH']['quote']['USD']['price']
        print(f"El precio actual de ETH es: ${price_eth:.2f}")
    except KeyError as e:
        print(e)



