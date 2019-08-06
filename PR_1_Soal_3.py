#Soal no 3: Given two two digit numbers, merge their digits as shown in the tests below
x=int(input('Angka Pertama: '))
y=int(input('Angka Kedua: '))

print('Gabungan kedua angka: '+str(x)+str(y))
x=str(x)
y=str(y)

print('Hasil pengacakan posisi angka: '+x[0]+y[0]+x[1]+y[1])

#Cara Lain
# a=int(input('Masukkan 2 angka pertama: '))
# b=int(input('Masukkan 2 angka kedua: '))
# tens_a=a//10
# units_a=a%10
# tens_b=b//10
# units_b=b%10
# print(tens_a+tens_b+units_a+units_b)