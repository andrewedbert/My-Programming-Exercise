# numList=[1,2,3]
# input ='x'
# check1 = input in numList
# check2 ='x' in ['x','y','z']
# check3 ='ka' in 'kurakas'
# print(check1)
# print(check2)
# print(check3)

def jumlah_kata(string):
    kata={}
    for word in string.lower().split():
        if word in kata.keys():
            kata[word]+=1
        else:
            kata[word]=1
    for keys, val in kata.items():
        print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(),val))

kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'

jumlah_kata(kata)