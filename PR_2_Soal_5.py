#Soal no 5 gambar *
x=''
for y in range(5,0,-1):
    for z in range(y):
        x+='   '
    for w in range(5-y):
        x+=' * '
    for m in range(4-y):
        x+=' * '
    x+='\n'
for y in range(1,5):
    for z in range(y):
        x+='   '
    for w in range(5-y):
        x+=' * '
    for m in range(4-y):
        x+=' * '
    x+='\n'

print(x)