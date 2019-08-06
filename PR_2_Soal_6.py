#Soal 6: Input Besar Bintang
x = int(input('Masukkan Besar Bintang : '))
y=''
z=''
for j in range (x,0,-1):
    for a in range (0,j):
        y += ' * '
    for b in range (0,x-j):
        y += '   '
    for c in range (0,(x-1)-j):
        y += '   '
    for d in range (0,j-1):
        y += '   '
    if (j==x):
        y += ''
    else:
        y += ' * '
    y += '\n'
for k in range (0,(x-1)):
    for e in range (0,k+2):
        z += ' * '
    for f in range (0,(x-2)-k):
        z += '   '
    for g in range (0,(x-3)-k):
        z += '   '
    for h in range (0,k+1):
        z += '   '
    if (k==(x-2)):
        z += ''
    else:
        z += ' * '
    z += '\n'
print(y+z)