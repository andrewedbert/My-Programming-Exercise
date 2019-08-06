#Soal no 1 gambar *
k=''

# for i in range(5):
#     for j in range(5-i):
#         k+=' * '
#     k+='\n'
# print(k)

for i in range(5,0,-1):
    for j in range(0,i):
        k+=' * '
    k+='\n'
print(k)