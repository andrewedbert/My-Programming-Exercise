a={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}
b={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}

c={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}
d={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}

e={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}
f={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}

g={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}
h={1:'o',2:'o',3:'o',4:'o',5:'o',6:'o',7:'o',8:'o',9:'o',10:'o'}

def MainMenu():
    option = int(input('Menu Utama:\n1. Pesan Tiket\n2. Lihat History\n3. Keluar\nPilihan Anda: '))
    return option

def PesanTiket():
    film=int(input('Daftar Film:\n1.Avengers: Endgame\n2. John Wick 3\nPilihan Anda: '))
    if film==1:
        SM=str(input('Siang/Malam: '))
        kali=int(input('Mau beli berapa? '))
        for x in range(kali):
            if SM=='Siang' or SM=='siang':
                Baris=int(input('Pilih Baris: '))
                if Baris==1:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(a[Kursi]=='x'):
                        a[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                elif Baris==2:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(b[Kursi]=='x'):
                        b[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                else:
                    print('Baris tidak tersedia')
                print(a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10])
                print(b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]+b[10])
            elif SM=='Malam' or SM=='malam':
                Baris=int(input('Pilih Baris: '))
                if Baris==1:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(c[Kursi]=='x'):
                        c[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                elif Baris==2:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(d[Kursi]=='x'):
                        d[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                else:
                    print('Baris tidak tersedia')
                print(c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+c[9]+c[10])
                print(d[1]+d[2]+d[3]+d[4]+d[5]+d[6]+d[7]+d[8]+d[9]+d[10])
    elif film==2:
        SM=str(input('Siang/Malam: '))
        kali=int(input('Mau beli berapa? '))
        for x in range(kali):
            if SM=='Siang' or SM=='siang':
                Baris=int(input('Pilih Baris: '))
                if Baris==1:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(e[Kursi]=='x'):
                        e[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                elif Baris==2:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(f[Kursi]=='x'):
                        f[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                else:
                    print('Baris tidak tersedia')
                print(e[1]+e[2]+e[3]+e[4]+e[5]+e[6]+e[7]+e[8]+e[9]+e[10])
                print(f[1]+f[2]+f[3]+f[4]+f[5]+f[6]+f[7]+f[8]+f[9]+f[10])
            elif SM=='Malam' or SM=='malam':
                Baris=int(input('Pilih Baris: '))
                if Baris==1:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(g[Kursi]=='x'):
                        g[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                elif Baris==2:
                    Kursi=int(input('Pilih Kursi: '))
                    if not(h[Kursi]=='x'):
                        h[Kursi]='x'
                    else:
                        print('Maaf sudah tidak tersedia')
                else:
                    print('Baris tidak tersedia')
                print(g[1]+g[2]+g[3]+g[4]+g[5]+g[6]+g[7]+g[8]+g[9]+g[10])
                print(h[1]+h[2]+h[3]+h[4]+h[5]+h[6]+h[7]+h[8]+h[9]+h[10])
    else:
        print('Film tidak tersedia')
    return x

def LihatHistory():
    print('Daftar Pesanan:')
    for x in a:
        if a[x]=='x':
            print('Avengers: Endgame siang pada baris 1 dan kursi {}'.format(x))
    for x in b:
        if b[x]=='x':
            print('Avengers: Endgame siang pada baris 2 dan kursi {}'.format(x))
    for x in c:
        if c[x]=='x':
            print('Avengers: Endgame malam pada baris 1 dan kursi {}'.format(x))
    for x in d:
        if d[x]=='x':
            print('Avengers: Endgame malam pada baris 2 dan kursi {}'.format(x))
    for x in e:
        if e[x]=='x':
            print('John Wick 3 siang pada baris 1 dan kursi {}'.format(x))
    for x in f:
        if f[x]=='x':
            print('John Wick 3 siang pada baris 2 dan kursi {}'.format(x))
    for x in g:
        if g[x]=='x':
            print('John Wick 3 malam pada baris 1 dan kursi {}'.format(x))
    for x in h:
        if h[x]=='x':
            print('John Wick 3 malam pada baris 2 dan kursi {}'.format(x))

Menu=[PesanTiket,LihatHistory]

while (True):
    option = MainMenu()
    if (option==1) or (option==2):
        Menu[option-1]()
    elif (option==3):
        print('Terima Kasih')
        break
    else:
        print('Menu tidak ada, silahkan pilih yang lain')