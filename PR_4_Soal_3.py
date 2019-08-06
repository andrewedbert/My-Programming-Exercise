def map(x,y):
    func=[x(i) for i in y]
    return func
list_kata=['Merdeka','Hello','Hellos','Sohib','Kari Ayam']

print(map(lambda x: x.lower(),list_kata))

def filterlist(function,list_container):
    hasil=[]
    for i in list_container:
        if function(i):
            hasil.append(i)
    return hasil

print(filterlist(lambda x: 'K' in x, list_kata))