def times2(num):
    return num*2

listNum=[1,2,3,4,5]
listNum=list(map(times2, listNum))
print(listNum)


listNum=[1,2,3,4,5]
listNum=list(map(lambda num: num*2, listNum))
print(listNum)

listNum=[1,2,3,4,5]
listNum=map(lambda num: num*2, listNum)
print(listNum)

def genap(num):
    return num%2==0

listNum=[1,2,3,4,5]
listNum=list(filter(genap,listNum))
print(listNum)

listNum=[1,2,3,4,5]
listNum=list(filter(lambda num:num%2==0,listNum))
print(listNum)

listNum=[1,2,3,4,5]
listNum=filter(lambda num:num%2==0,listNum)
print(listNum)