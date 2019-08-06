# Soal no. 1
def nb_year(p0, percent, aug, p):
    abs(p0)
    abs(p)
    int(aug)
    percent = abs(percent)/100
    year = 0
    while(True):
        if p0 >= p:
            break
        else:
            p0 = round((p0 + (p0*percent) + aug))
            year += 1
    print('Year(s) need to surpass the target population is {}'.format(year))   

nb_year(1000, 2, 50, 1200)

#Soal 2
peopleInLine = [25, 25, 100, 50, 75]
def tickets(peopleInLine):
    list = []
    money = {}
    idx = [25,50,75,100]
    for i in idx:
        money.setdefault(i, 0)
    for j in peopleInLine:
        if j == 25:
            money[25] += 1
            list.append(j)
        elif j == 50 and money[25] > 0:
            money[25] -= 1
            money[50] += 1
            list.append(j)
        elif j == 50 and money[25] == 0:
            print('NO')
            break
        elif j == 75 and money[50] >= 1:
            money[75] += 1
            money[50] -= 1
            list.append(j)
        elif j == 75 and money[25] >= 2:
            money[75] += 1
            money[25] -= 2
            list.append(j)
        elif (j == 75 and money[25] <= 1) or (j == 75 and money[50] == 0):
            print('NO')
            break
        elif j == 100 and money[75] >= 1:
            money[100] += 1
            money[75] -= 1
            list.append(j)
        elif j == 100 and money[50] >= 1 and money[25] >= 1:
            money[100] += 1
            money[50] -= 1
            money[25] -= 1
            list.append(j)      
        elif j == 100 and money[25] >= 3:
            money[100] += 1
            money[25] -= 3
            list.append(j)
        else:
            print('NO')
            break            
    if len(list) == len(peopleInLine):
        print('YES')
                  
tickets(peopleInLine)

# #Soal Nomor 3
def rowSumOddNumbers(n):
    z = ''
    odd = list(filter(lambda x: x%2 != 0, list(map(lambda x: x+1, range(n**3)))))
    odd_list = []
    var = 0
    if n == 1:
        odd_list = [1]
    else:
        for i in range(n):
            var += i+1    
    for j in range(var):
        odd_list.append(odd[j])
    num = []
    for k in odd_list:
        num.append(str(k))  
    idx = 0
    for i in range (0,n):
        for j in range (0, (len(odd_list))):
            if j >= len(odd_list)-i and j <= len(odd_list)+i:
                z += ' ' +str(odd_list[idx])+' '
                idx += 1
            else: 
                z += '   '    
        z += '\n'
    print(z)
    print(sum(odd_list))    

rowSumOddNumbers(3)