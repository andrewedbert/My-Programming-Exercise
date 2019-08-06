def FizzBuzz(x):
    for x in range(1,x+1):
        if (x%3==0) and (x%5==0):
            print('FizzBuzz')
        elif (x%3==0) and (not(x%5==0)):
            print('Fizz')
        elif (not(x%3==0)) and (x%5==0):
            print('Buzz')
        else:
            print(x)

# FizzBuzz(100)

# y=int(input('Masukkan angka fibonacci: '))
def Fibonacci(y):
    z=[1,1]
    for i in range(2,y):
        z.append((z[i-2])+(z[i-1]))
    print(list(z))
    return print('Fibonacci number {} adalah {}'.format(y,(z[y-1])))

# Fibonacci(y)

# x=[6000,34,203,3,746,200,984,198,764,9,1]

def bubbleSort(list):
    for i in range(len(list),0,-1):
        for j in range(0,i-1):
            if (list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

# print (bubbleSort(x))

a=[1,2,3,2,3,2,3]

def mean(a):
    b=0
    for c in a:
        b+=c
    mean=b/(len(a))
    print(mean)
mean(a)

def median(a):
    bubbleSort(a)
    j=len(a)//2
    k=len(a)%2
    if k == 0:
        print(a[j])
    else:
        med=(a[j]+(a[j+1]))/2
        print(med)
median(a)

def Mode(a) :
    count = {}
    for x in a :
        if(x in count.keys()) :
            count[x] += 1
        else :
            count[x] = 1
    F_Max = 1
    modes = []
    for y in count :
        if (count[y] > F_Max) :
            modes = [y]
            F_Max = count[y]
        elif (count[y] == F_Max) :
            modes.append(y)
    if (len(modes) == len(count.keys())) :
        modes = []
    print(modes)

Mode(a)
