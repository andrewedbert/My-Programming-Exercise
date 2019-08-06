import requests

host = 'https://developers.zomato.com/api/v2.1'
cari = input('Kamu mau makan apa? ')
url = f'{host}/search?entity_id=74&q={cari}'
apikey = '3d7c47e9b1cd0f9a62bc1a4777460b18'
headers = {
    'user-key' : apikey,
}

data = requests.get(url, headers=headers)
listResto = data.json()['restaurants']
for i in listResto:
    print(
        i['restaurant']['name'], ':',
        i['restaurant']['location']['address']
    )
# print(listResto)