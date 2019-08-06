x=float(input("Masukkan berat badan dalam kg: "))
y=float(input("Masukkan tinggi badan dalam meter: "))

z=x/(y**2)

print("IMT anda: "+str(z))

if(z<18.5):
    print("Berat Badan Kurang")
elif(z>=18.5 and z<=24.9):
    print("Berat Badan Ideal")
elif(z>=25.0 and z<=29.9):
    print("Berat Badan Berlebih")
elif(z>=30.0 and z<=39.9):
    print("Berat Badan Sangat Berlebih")
else:
    print("Obesitas")