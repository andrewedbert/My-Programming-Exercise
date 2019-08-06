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

# tower_builder(3,(2,3))
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
expandedForm(901176)

# def rangenum(x,y):
#     nl=''
#     for m in range(x, y):
#         if (m%7==0) and (m%5==0):
#             nl+=str(m)+'\n'
#     print (nl)

# rangenum(1500,2700)

# def expanded_form(num):
#     result = []

#     for index, digit in enumerate(str(num)[::-1]):
#         if int(digit) != 0:
#             result.append(digit + ('0' * index))

#     return print(' + '.join(result[::-1]))

# expanded_form(12)
# expanded_form(42)
# expanded_form(70304)

# def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
#     months = 0
#     savings = 0

#     while startPriceOld + savings < startPriceNew:
#         months += 1
#         savings += savingperMonth

#         if months % 2 == 0:
#             percentLossByMonth += 0.5
#             print('this is the month: ', months)

#         startPriceOld *= ((100 - percentLossByMonth) / 100)
#         startPriceNew *= ((100 - percentLossByMonth) / 100)

#     print([months, round(startPriceOld + savings - startPriceNew)])

# nbMonths(12000, 8000, 1000, 1.5)
# nbMonths(8000, 8000, 1000, 1.5)