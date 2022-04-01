import requests
# price of 1 ETH to USD
# api-endpoint of etherminer
URL = "https://api.ethermine.org/miner/{Your ETH Adress}/currentStats"
URL_ETH="https://api.coinbase.com/v2/prices/ETH-USD/sell/"

r = requests.get(URL_ETH)
data_json = r.json()
data = dict(data_json)
# 2288 on january 2021
ETH2USD = data['data']['amount']

# sending get request and saving the response as response object
r = requests.get(URL)

# extracting data in json format
data_json = r.json()
data = dict(data_json)

format_unpaid = int(data['data']['unpaid'])
