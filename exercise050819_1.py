import json
import csv

# # Read JSON
# with open('data.json') as x:
#     data = json.load(x)

# Read CSV
data=[]
with open('data.csv', 'r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))
print(data)

# Write JSON
with open('x.json', 'w') as x:
    json.dump(data, x)

# # Write CSV
# with open('x.csv', 'w', newline='') as x:
#     kolom = list(data[0].keys())
#     tulis = csv.DictWriter(x, fieldnames=kolom)
#     tulis.writeheader()
#     tulis.writerows(data)