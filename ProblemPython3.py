x=485
y=x//365
z=(x%365)//30
w=((x%365)%30)//7
m=((x%365)%30)%7

print(str(x)+' Hari itu sama dengan '+str(y)+' Tahun, '+str(z)+' Bulan, '+str(w)+' Minggu, '+str(m)+' Hari')