x=(input('Masukkan angka: '))
y=''

for i in range(3):
    if i == 0:
        for m in x:
            if m=='0':
                y+=' _ '
            elif m=='2':
                y+=' _ '
            elif m=='3':
                y+=' _ '
            elif m=='5':
                y+=' _ '
            elif m=='6':
                y+=' _ '
            elif m=='7':
                y+=' _ '
            elif m=='8':
                y+=' _ '
            elif m=='9':
                y+=' _ '
            else:
                y+='   '
    elif i==1:
        for m in x:
            if m=='0':
                y+='| |'
            elif m=='1':
                y+='  |'
            elif m=='2':
                y+=' _|'
            elif m=='3':
                y+=' _|'
            elif m=='4':
                y+='|_|'
            elif m=='5':
                y+='|_ '
            elif m=='6':
                y+='|_ '
            elif m=='7':
                y+='  |'
            elif m=='8':
                y+='|_|'
            elif m=='9':
                y+='|_|'
            else:
                y+='   '
    elif i==2:
        for m in x:
            if m=='0':
                y+='|_|'
            elif m=='1':
                y+='  |'
            elif m=='2':
                y+='|_ '
            elif m=='3':
                y+=' _|'
            elif m=='4':
                y+='  |'
            elif m=='5':
                y+=' _|'
            elif m=='6':
                y+='|_|'
            elif m=='7':
                y+='  |'
            elif m=='8':
                y+='|_|'
            elif m=='9':
                y+=' _|'
            else:
                y+='   '
    y+='\n'
print(y)