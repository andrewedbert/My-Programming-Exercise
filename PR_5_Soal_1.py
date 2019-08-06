def mainMenu(theList) : 
    while True :
        show(theList)
        iDirection = input('Mau diputar ke Kanan atau ke Kiri? : ')
        iTimes = input('Mau diputar berapa kali? : ')
        theList = putar(iDirection, int(iTimes), theList)
        iStop = input('Input 1 untuk keluar lain untuk lanjut : ')
        if(iStop == '1'):
            break
    
def show(theList) :
    outPut = ''
    for i in range(4) :
        outPut += '\n'
        for j in range(4) :
            outPut += (' ' + str(theList[i][j]))
    print(outPut)


def putar(arah, iTimes, arr) :
    kali = iTimes % 4
    newArr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    if(kali == 0) :
        newArr = arr

    elif((kali == 1 and arah == 'Kanan') or (kali == 3 and arah == 'Kiri')) :
        for i, k in (range(4), range(3,-1,-1)) :
            for j in range(4) :
                newArr[j][k] = arr[i][j]

    elif(kali == 2) :
        for i, k in (range(4), range(3,-1,-1)) :
            for j, l in (range(4), range(3,-1,-1)) :
                newArr[k][l] = arr[i][j]

    elif((kali == 3 and arah == 'Kanan') or (kali == 1 and arah == 'Kiri')) :
        for i in range(4) :
            for j, l in (range(4), range(3,-1,-1)) :
                newArr[l][i] = arr[i][j]

    show(newArr)
    return newArr

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

mainMenu(list1)