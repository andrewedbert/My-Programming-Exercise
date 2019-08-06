#Soal no 5: Given a string consisting of exactly two words separated by a space. Print a new string with the first and second word positions swapped
x="Makan Hati"

print(x[6:]+' '+x[:5])

# Cara Lain
a=input('Masukkan Kata: ')
lis=a.split()
print(lis[1]+' '+lis[0])
