listNum=[1,2,3,4,5]
listNum=[item*2 for item in listNum]
print(listNum)

for idx, val in enumerate(['Kucing','Habis','Bakar','Makan','Minum']):
    print(idx)
    print(val)

kata={idx:val for idx, val in enumerate(['Kucing','Habis','Bakar','Makan','Minum'])}

print(kata)