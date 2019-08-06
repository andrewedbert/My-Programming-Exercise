def mainMenu() :
    b=input('Main Menu : \n 1. Lihat Full Dictionary \n 2. Isi Dictionary \n 3. Searching Dictionary \n 4. Keluar \n\n Pilih : ')
    return b

def lihatFullDictionary(Dict) :
    print('Full Dictionary : ')
    print('..........................................')
    print('|        Key         |       Value       |')
    print('|....................|...................|')
    for key in Dict :
        if((type(Dict[key])) == type('')) :
            print('|        ' + key + '        |        ' + Dict[key] + '        |')
        elif((type(Dict[key])) == (0)) :
            print('|        ' + key + '         |       ' + str(Dict[key]) + '        |')
        print('|....................|...................|')

def isiDictionary(Dict) :
    iK = input('Isi Key : ')
    iT = input('Value input 1 untuk string, 2 untuk number? : ')
    if(iT == '1') :
        iV = input('Valuenya : ')
        Dict[iK] = iV
    elif(iT == '2') :
        iV = int(input('Valuenya : '))
        Dict[iK] = iV
    else :
        print('Kesalahan fatal!')

def searchDictionary(Dict) :
    iS = input('Key search : ')
    nDict = {}
    for key in Dict:
        if(iS.lower() in key.lower()) :
            nDict[key] = Dict[key]

    lihatFullDictionary(nDict)


nDict2 = {}

LM=[lihatFullDictionary, isiDictionary, searchDictionary]
while True :
    c=int(mainMenu())
    if(c==4) :
        print('Terima kasih')
        break
    elif(c>=1 and c<=3):
        LM[int(c)-1](nDict2)
    else:
        print('Menu tidak terdaftar')