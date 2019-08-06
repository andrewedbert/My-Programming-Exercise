import csv

# data = [
#     ['Andi', '12345'],
#     ['Budi', '12346'],
#     ['Caca', '12347']
# ]

# data = [
#     {'nama':'Andi','nis':'12345'},
#     {'nama':'Budi','nis':'12346'},
#     {'nama':'Caca','nis':'12347'}
# ]

# data = ['Andi','Budi','Caca']
# with open('fileku.csv', 'w', newline='') as x:
#     writer = csv.writer(x, delimiter='\\')
#     for nama in data:
#         writer.writerow(nama)

# with open('fileku.csv', 'w', newline='') as x:
#     writer = csv.DictWriter(x, fieldnames=['nis','nama'])
#     writer.writeheader()
#     writer.writerows(data)

data=[]
with open('fileku.csv', 'r', newline='') as x:
    reader = csv.DictReader(x)
    for i in reader:
        # print(dict(i))
        data.append(dict(i))
print(data)