#Soal no 1: Given a four digit number, perform its cyclic rotation by two digits
x=int(input("Masukkan Angka: "))

x=str(x)

print(x[2:]+x[:2])

#Cara Lain
# a=int(input("Masukkan Angka: "))

# print(a%100*100+a//100)