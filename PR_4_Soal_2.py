# daftar=['Merdeka','Hello','Hellos','Sohib','Ayam']
# print(daftar)
# x=str(input('Search: '))

# a=x in daftar

# print(a)

x=['Merdeka','Hello','Hellos','Sohib','Kari Ayam']
y=[]
z=str(input('Kata yang ingin dicari: '))

for m in range(len(x)):
    if z in x[m].lower():
        y.append(x[m])
    elif z in x[m].upper():
        y.append(x[m])

print(y)