# Segitiga Berlubang
z= ''
for i in range (0,10,1):
    if i < 9:
        for j in range (0, 21):
            if j == 10-i or j == 10+i:
                z += ' * '
            else: 
                z += '   '    
        z += '\n'
    else:
        for j in range (0, 21):
            if j > 0 and j < 20:
                z += ' * '
            else: 
                z += '   '
print (z)

# Persegi Berlubang
# z= ''
# for loop in range(5):
#     for loop2 in range(5):
#         # if (loop>0 and loop<4) and (loop2>0 and loop2<4):
#         #     z+='   '
#         # else:
#         z+=' * '
#     z+='\n'
# print(z)


# z= ''
# for item in range(4):
#     for item1 in range(0,item):
#         z += '*'
#     z+='\n'
# print(z)