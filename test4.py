# solve 1
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(5):
#     for num1 in range(num,5):
#         z += " * "
#     z += "\n"

# print(z)

# solve 2
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * "
#     z += "\n"
# for num in range(size-1):
#     for num1 in range(num+2):
#         z += " * "
#     z += "\n"

# print(z)

# solve 3
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(size-1-num):
        z += "   "
    for num2 in range((num*2)+1):
        z += " * "
    z += "\n"

print(z)

# solve 4
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(size):
#     for num1 in range(num):
#         z += "   "
#     for num2 in range((size*2)-(num*2)-1):
#         z += " * "
#     z += "\n"

# print(z)

# solve 5
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(size):
#     for num1 in range(size-1-num):
#         z += "   "
#     for num2 in range((num*2)+1):
#         z += " * "
#     z += "\n"
# for num in range(1, size):
#     for num1 in range(num):
#         z += "   "
#     for num2 in range((size*2)-(num*2)-1):
#         z += " * "
#     z += "\n"

# print(z)

# solve 6
# size = int(input("Masukkan size: "))
# z = ""

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * "
#     for num2 in range(0, (num*2)-1):
#         z += "   "
#     for num3 in range(size, num, -1):
#         if(num3 == 1):
#             break
#         z += " * "
#     z += "\n"
# for num in range(size-1):
#     for num1 in range(0, num+2):
#         z += " * "
#     for num2 in range(size*2-5, num*2, -1):
#         z += "   "
#     for num3 in range(0, num+2):
#         if(num == size-2 and num3 == num+1):
#             break
#         z += " * "
#     z += "\n"

# print(z)

# def rowSumOddNumbers(n) :
#     theList = []
#     nilai = 1

#     for i in range(1, n+1) :
#         rowList = []
#         for j in range(i) :
#             rowList.append(nilai)
#             nilai += 2
#         theList.append(rowList)

#     return theList

# row = 10
# listHasil = rowSumOddNumbers(row)
# print(sum(listHasil[-1]))

# z = ''
# for listRow, i in zip(listHasil, range(len(listHasil))) :
#     for j in range(row-i) :
#         z += '  '
#     for num in listRow :
#         z += str(num).ljust(4)
#         # z += str(num)
#         # for k in range(4 - len(str(num))) :
#         #     z += ' '
#     z += '\n'

# print(z)

# def tickets(peopleInLine):
#     duitKembaliVasya = { "50": 0, "25": 0 }
#     hargaTiket = 25
#     check = "YES"

#     for duitCustomer in peopleInLine :
#         kembali = duitCustomer - hargaTiket
#         if(kembali == 0) :
#             duitKembaliVasya["25"] += 1
#         elif(kembali == 25) :
#             if(duitKembaliVasya["25"] == 0) :
#                 check = "NO"
#                 break
#             duitKembaliVasya["25"] -= 1
#             duitKembaliVasya["50"] += 1
#         elif(kembali == 75) :
#             if(duitKembaliVasya["50"] > 0 and duitKembaliVasya["25"] > 0) :
#                 duitKembaliVasya["50"] -= 1
#                 duitKembaliVasya["25"] -= 1
#             elif(duitKembaliVasya["25"] > 2) :
#                 duitKembaliVasya["25"] -= 3
#             else :
#                 check = "NO"
#                 break

#     return check

# print(tickets([25,25,25,100,75]))

# def nbYear(p0, percent, aug, p) :
#     year = 0
#     while p0 < p :
#         p0 = p0 + (p0 * percent/100) + aug
#         year += 1
    
#     return year

# print(nbYear(1000,2,50,1200))
