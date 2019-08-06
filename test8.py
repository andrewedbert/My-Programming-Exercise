import requests

url = 'https://blockchain.info/ticker'
data = requests.get(url)
listrate=data.json()
print(listrate['USD']['sell'])