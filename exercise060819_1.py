import requests

apikey = 'a3515f2287ffb8f930d39233c31465fa'
kota = input('Ketik nama kota: ')
host = 'api.openweathermap.org'
url = f'http://{host}/data/2.5/weather?q={kota}&APPID={apikey}'


data = requests.get(url)
cuaca = data.json()

if data.status_code == 200:
    print(cuaca['name'])
    print(cuaca['weather'][0]['main'], cuaca['weather'][0]['description'])
    print(round(cuaca['main']['temp'] - 273, 2), 'C')
    print(cuaca['main']['humidity'], '%')
    print(cuaca['main']['pressure'], 'bar')
else:
    print('Maaf, kota tidak terdaftar')