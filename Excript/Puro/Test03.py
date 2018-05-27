altura=float(input("Informe sua altura: "))
peso=float(input("Informe seu peso: "))
imc=peso/(altura**2)
print("Seu IMC é %.2f"%imc)

if(imc<20):
    print("Abaixo do peso")

elif(imc>=20 and imc<25):
    print("Peso ideal")

elif(imc>=25 and imc<30):
    print("Sobrepeso")

elif(imc>=30 and imc<35):
    print("Obesidade moderada")

elif(imc>=35 and imc<40):
    print("Obesidade severa")

elif(imc>=40 and imc<50):
    print("Obesidade morbida")

else:
    print("Peso ideal")