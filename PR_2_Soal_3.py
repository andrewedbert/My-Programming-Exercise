#Soal no 3 gambar *
x=''

for y in range(10,0,-1):
    for z in range(y):
        x+='   '
    for w in range(10-y):
        x+=' * '
    for m in range(9-y):
        x+=' * '
    x+='\n'

print(x)