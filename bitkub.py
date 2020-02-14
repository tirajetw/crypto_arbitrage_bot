import time
import json
import requests

url = "https://api.bitkub.com/api/market/ticker"
print ("Request JSON from : " + url)
response = requests.get(url)
data = response.json()

print (data["THB_BTC"]["last"])

# json_data = json.loads(response.read())
# for k, v in json_data.items():
#     print(k, v)