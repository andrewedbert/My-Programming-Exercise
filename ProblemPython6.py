s=int(input('Jarak A dan B: '))
a=int(input('Kecepatan mobil A:'))
b=int(input('Kecepatan mobil B:'))

x=(b*s)/(a+b)
y=x/b

c=y*60
h=c+(9*60)
f=h//60
w=h%60

f=int(f)
w=int(w)

print('Mobil A dan Mobil B akan bertabrakan pada pukul '+str(f)+' lewat '+str(w)+ ' menit')