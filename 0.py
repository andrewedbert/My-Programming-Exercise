# myFile = open('test.csv','r')
# # print(myFile.readable())
# # print(myFile.read())
# print(myFile.readlines())

# data=[]
# for i in myFile.readlines():
#     data.append(i.split('\n')[0])

# print(data)

myFile = open('test.csv','w')

myFile.write('Doni')

myFile = open('test.csv','r')

print(myFile.readlines())

data = ['Budi','Caca','Didi Kempot']
myFile = open('students.csv','a')
myFile.write('Andi')
for i in data:
    myFile.write('\n'+i)

myFile = open('students.csv','r')

print(myFile.readlines())