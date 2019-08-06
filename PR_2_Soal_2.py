#Soal no 2 gambar *
x=''

for y in range(5,0,-1):
    for z in range(0,y):
        x+=' * '
    x+='\n'
for y in range(1,5):
    for z in range(y+1):
        x+=' * '
    x+='\n'
print(x)