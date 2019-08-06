import json
import csv
with open('data.json') as x:
    data = json.load(x)

# print(data)
# print(type(data))

# read JSON => write CSV
# read CSV => JSON
with open('baru.csv', 'w', newline='') as x:
    writer = csv.DictWriter(x, fieldnames=['nama','usia'])
    writer.writeheader()
    writer.writerows(data)

newData=[]
with open('baru.csv', 'r', newline='') as x:
    reader = csv.DictReader(x)
    for i in reader:
        newData.append(dict(i))

# print(newData)

with open('baru.json', 'w') as x:
    a=str(newData)
    x.write(a.replace("'",'"'))

# print(a)

with open('x.json', 'w') as x:
    json.dump(data, x)