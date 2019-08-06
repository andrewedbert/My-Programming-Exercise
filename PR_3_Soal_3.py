# #Soal 3 Menu Array
# def fungsi_menu():
#     print('Main Menu:')
#     print('1. Isi Array')
#     print('2. Lihat Array')
#     print('3. Sort Array')
#     print('4. Nilai tertinggi dan terendah')
#     print('5. Jumlah Ganjil dan Genap')
#     print('6. Keluar')
#     i=(input('Pilih Menu: '))
#     if (int(i)==1):
#         isi_array()
#         return isi_array()
#     # elif(int(i)==2):
#     #     lihat_array()
#     #     return lihat_array()
#     elif(int(i)==6):
#         print('Sampai Jumpa')
#     else:
#         print('Pilihan menu tidak ada')
#         fungsi_menu()


# def isi_array():
#     x=[]
#     a=int(input('Masukkan jumlah angka: '))
#     mat=x.append(a)
#     for item in (x):
#         while (a<=x):
#             print(a)
#             a+=1
#     return fungsi_menu()

# # def lihat_array():
# #     print(isi_array())
# # print('List angka: {}'.format(arr_1))

# # def fungsi_ascending(arr):
# #     for x in range(len(arr)):
# #         for y in range(x+1,len(arr)):
# #             if arr[x]>arr[y]:
# #                 arr[x],arr[y]=arr[y],arr[x]
# #     return arr

# # print(fungsi_ascending(arr_1))

# # def fungsi_descending(arr):
# #     for x in range(len(arr)):
# #         for y in range(x+1,len(arr)):
# #             if arr[x]<arr[y]:
# #                 arr[x],arr[y]=arr[y],arr[x]
# #     return arr

# # print(fungsi_descending(arr_1))

# # def minimum(arr):
# #     start = arr[0]
# #     for x in (arr):
# #         if start > x:
# #             start=x
# #     return start

# # print('Nilai minimum: {}'.format(minimum(arr_1)))

# # def maximum(arr):
# #     stop = arr[0]
# #     for x in (arr):
# #         if stop < x:
# #             stop=x
# #     return stop

# # print('Nilai maximum: {}'.format(maximum(arr_1)))

# fungsi_menu()

arr = []

def MainMenu() :
    pilihan = int(input("Menu : \n 1. Isi Array \n 2. Lihat Array \n 3. Sort Array \n 4. Nilai Min Max \n 5. Genap Ganjil \n 6. Exit \nYour Choice? : "))
    return pilihan

def SeeArray() :
    print('Isi Array : ')
    print(arr)

def InputArray() :
    y= int(input('Jumlah Angka: '))
    for num in range(y):
        num = int(input('Number : '))
        arr.append(num)

def Ascending(a,b) :
    return a - b

def Descending(a,b) :
    return b - a

Sort=[Ascending,Descending]

def SortArray() :
    option_S = int(input('Input 1 untuk Ascending dan 2 untuk Descending : '))
    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)) :
            if(Sort[option_S-1](arr[i], arr[j]) > 0) :
                temp = arr[i]
                arr[i] = arr[j] 
                arr[j] = temp 

def MinMaxArray() :
    minNum = arr[0]
    maxNum = arr[0]
    for num in arr[1:] :
        if(num < minNum) :
            minNum = num
        if(num > maxNum) :
            maxNum = num
    print("Min : {} and Max : {}".format(minNum,maxNum))

def OddEven():
    x=arr[0]
    for x in arr[0:]:
        if x%2 == 0:
            print(str(x)+' Bilangan Genap')
        else:
            print(str(x)+' Bilangan Ganjil')

F_List = [InputArray,SeeArray,SortArray,MinMaxArray,OddEven]

while(True) :
    pilihan = MainMenu()
    if(pilihan == 1 or pilihan == 2 or pilihan == 3 or pilihan == 4 or pilihan == 5) :
        F_List[pilihan-1]()
    elif(pilihan == 6) :
        print('Sampai Jumpa Lagi!')
        break