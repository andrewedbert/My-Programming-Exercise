text=input('kata: ')
find=input('karakter yang ingin dicari: ')

print(text.split(find))
print(int(len(text.split(find)))-1)