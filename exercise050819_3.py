import requests

team = input('Ketik Tim: ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='
url2= url+team
print(url2)
data = requests.get(url2)
players = data.json()['player']
# print(players)

for player in players:
    print(player['strPlayer'])