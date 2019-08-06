# x=int(input('Masukkan jumlah baris angka: '))
# angka=0
# while (angka<=x):
#     print(angka)
#     angka+=1

# s='banana sdasd nans banana'
# b='banana'
# def count_words(s,b):
#     answer = 0
#     counter = 0
#     if b in s:
#         for i in range(len(s)):
#             if s[i]!=b[counter]:
#                 counter=0
#             else:
#                 counter+=1
#             if counter == len(b):
#                 answer+=1
#                 counter = 0
#     print(answer)

# count_words(s, b)

# def Sequential_Search(dlist, item):

#     pos = 0
#     found = False
    
#     while pos < len(dlist) and not found:
#         if dlist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
    
#     return found, pos

# print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))

#Pangkat Tanpa Pow()
# def pangkat(num,pow):
#   number = 1
#   for x in range(pow):
#     number=number*num
#   return number

# print(pangkat(10,5))

#Seven Segment
# inputUser = input('Masukkan angka : ')

# arr = inputUser.split(' ')
# # # arr = ['1', '2', '3', '4', '5', '6', '7' '8', '8','8', '9', '0', '']
# output = ''
# # dict1 = { '1': '   ', '2': ' _ ', '3': ' _ ' }
# # dict2 = { '1': '  |', '2': ' _|', '3': ' _|' }
# # dict3 = { '1': '  |', '2': '|_ ', '3': ' _|' }

# for i in range(3) :
#     if(i == 0) :
#         for item in arr :
#             if(item == '2' or item == '3' 
#                 or item == '5' or item == '6' 
#                 or item == '7' or item == '8' 
#                 or item == '9' or item == '0') :
#                 output += ' _ '
#             else :
#                 output += '   '
#     elif(i == 1) :
#         for item in arr :
#             if(item == '8' or item == '9' or item == '4') :
#                 output += '|_|'
#             elif(item == '2' or item == '3') :
#                 output += ' _|'
#             elif(item == '5' or item == '6') :
#                 output += '|_ '
#             elif(item == '1' or item == '7' ) :
#                 output += '  |'
#             else :
#                 output += '| |'
#     elif(i == 2) :
#         for item in arr :
#             if(item == '8' or item == '0' or item == '6') :
#                 output += '|_|'
#             elif(item == '5' or item == '3' or item == '9') :
#                 output += ' _|'
#             elif(item == '2') :
#                 output += '|_ '
#             else :
#                 output += '  |'
#     output += '\n'

# print(output)

#Reverse using math function
# import math

# def reverseList(theList) :
#     for i in range(0, math.floor(len(theList)/2)) :
#         theList[i], theList[len(theList) - 1 - i] = theList[len(theList) - 1 - i], theList[i]

#     return theList

# print(reverseList([1,2,3,4,5,6,7,8,9]))
# print(reverseList(['anto','agus','hila','koko','lidah','cinlok','paru','hati','jantung']))

def power(num,pow):
  number = 1
  for x in range(pow):
    number=number*num
  return number

print(power(3,4))

def p(base, exp):
    res = 1
    for _ in range(exp):
        res *= base
    return res

print(p(3,5))