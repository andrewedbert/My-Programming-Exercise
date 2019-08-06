# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     x=''
#     for o in range(n_floors):
#         for k in range(h):
#             for u in range(o,n_floors+1):
#                 x+='  '
#             for c in range(w):
#                 x+='*'
#             x+='\n'
#         w=w+4
#     print(x)

# tower_builder(5,(3,3))
# tower_builder(6,(2,1))

def expandedForm(num):
    string=str(num)
    hasil=''

    for loop in range(len(string)):
        x=(len(string)-loop-1)*str(0)
        if int(string[loop])!=0:
            y=string[loop]+x
            if (int(loop)+1)!=int(len(string)):
                hasil+=y+' + '
            else:
                hasil+=y
    print(hasil)

expandedForm(12)
expandedForm(42)
expandedForm(70304)