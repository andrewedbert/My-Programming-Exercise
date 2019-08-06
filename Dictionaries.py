# d={"key1":"item1","key2":"item2","kucing":[3,"jerapah"]}

# print(d["key1"])
# print(d["key2"])
# print(d["kucing"])
# print(d["kucing"][1])

d={'key1':{'key2':'item2'},'kucing':[3,'jerapah']}

print(d['key1'])
print(d['key1']['key2'])
print(d['kucing'])
print(d['kucing'][1])
# print(d.keys())
# print(d.values())
# print(d.items())

for i in d.items():
    print(i)

for key, val in d.items():
    print('Ini key {} dan value {}'.format(key,val))