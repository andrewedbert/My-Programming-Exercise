import requests

def MainMenu():
    option=int(input('Selamat Datang\nSilahkan pilih konversi yang akan Anda lakukan :\n (1) IDR Indonesia => USD United States\n (2) USD United States => IDR Indonesia\nPilihan Anda (1/2): '))
    return option

def IDRtoUSD():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        kursjual = float(data.json()['jual'])
        kursbeli = float(data.json()['beli'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: Rp. '))
        hasilkonversi = nilaiuang/kursjual
        print('Hasil konversi Rp. {} adalah USD {}'.format(nilaiuang,hasilkonversi))
        print('Dengan kurs jual Rp. {} dan kurs beli Rp. {}'.format(kursjual,kursbeli))


def USDtoIDR():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        kursjual = float(data.json()['jual'])
        kursbeli = float(data.json()['beli'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: USD '))
        hasilkonversi = nilaiuang*kursbeli
        print('Hasil konversi USD {} adalah Rp. {}'.format(nilaiuang,hasilkonversi))
        print('Dengan kurs jual Rp. {} dan kurs beli Rp. {}'.format(kursjual,kursbeli))

Menu=[IDRtoUSD,USDtoIDR]

# while True:
#     option=MainMenu()
#     if option == 1 or option == 2:
#         Menu[option-1]()
#     elif option == 3:
#         break

option=MainMenu()
if option == 1:
    Menu[0]()
elif option == 2:
    Menu[1]()