# mobil=['Alya','Xenia','Avanza']

# print(mobil)
# print(mobil[0])
# print(mobil[1])
# print(mobil[2])
# print(mobil[3])

#Access List Value

# buah = ['Jeruk','Nanas','Apel']

# for item in buah:
#     print(item)

# buah=['Jeruk','Nanas','Apel','Mangga']

# print(buah[1:])
# print(buah[:3])
# print(buah[2:4])
# print(buah[:])

# buah[1]='Kelapa'
# print(buah)

#List append & pop

# buah=['Jeruk','Nanas','Apel','Mangga']

# buah.append('Kelapa')
# print(buah)
# buah.pop()
# buah.pop()
# print(buah)

#List inside List and Diff Type Data

# listTest=[1,'hi',['hello',2,True,[0,1]]]

# print(listTest[1])
# print(listTest[:2])
# print(listTest[2])
# print(listTest[2][1:])
# print(listTest[2][2])
# print(listTest[2][3][0])

list_test=[1,3,4]
print(list_test)
list_test[0],list_test[2]=list_test[2],list_test[0]
print(list_test)