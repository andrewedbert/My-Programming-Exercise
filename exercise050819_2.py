import csv
import json

with open('data.json') as x:
    dataJson = json.load(x)

dataCsv=[]
with open('data.csv','r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        dataCsv.append(dict(i))

# dataJson=[]
# dataCsv=[]
nama = input('Ketik Nama: ')
usia = input('Ketik Usia: ')
kota = input('Ketik Kota: ')

newData= {
    'nama':nama,
    'usia':usia,
    'kota':kota
}

dataJson.append(newData)
dataCsv.append(newData)
print(dataJson)
print(dataCsv)

with open('data.json','w') as x:
    json.dump(dataJson,x)

with open('data.csv', 'w', newline='') as x:
    kolom = list(dataCsv[0].keys())
    tulis = csv.DictWriter(x, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(dataCsv)