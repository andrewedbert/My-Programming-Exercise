#Fungsi Sort Soal 1 dan 2
arr_1=[40,100,1,5,25,10]

def fungsi_ascending(arr):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x]>arr[y]:
                arr[x],arr[y]=arr[y],arr[x]
    return arr

print(fungsi_ascending(arr_1))

def fungsi_descending(arr):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x]<arr[y]:
                arr[x],arr[y]=arr[y],arr[x]
    return arr

print(fungsi_descending(arr_1))

def minimum(arr):
    start = arr[0]
    for x in (arr):
        if start > x:
            start=x
    return start

print('Nilai minimum: {}'.format(minimum(arr_1)))

def maximum(arr):
    stop = arr[0]
    for x in (arr):
        if stop < x:
            stop=x
    return stop

print('Nilai maximum: {}'.format(maximum(arr_1)))