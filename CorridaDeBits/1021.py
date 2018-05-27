num = float(input())

moedas = int((num-int(num))*100)
num = int(num)

#Cálculo do menor número de notas 
n100 = num//100
num -= n100*100

n50 = num//50
num -= n50*50

n20 = num//20
num -= n20*20

n10 = num//10
num -= n10*10

n5 = num//5
num -= n5*5

n2 = num//2
num -= n2*2

#Cálculo do menor número de moedas

m50 = moedas//50
moedas -= m50*50

m25 = moedas//25
moedas -= m25*25

m10 = moedas//10
moedas -= m10*10

m5 = moedas//5
moedas -= m5*5

#Impressão dos valores das notas

print("NOTAS:")
print(n100,"nota(s) de R$ 100.00")
print(n50,"nota(s) de R$ 50.00")
print(n20,"nota(s) de R$ 20.00")
print(n10,"nota(s) de R$ 10.00")
print(n5,"nota(s) de R$ 5.00")
print(n2,"nota(s) de R$ 2.00")

#Impressão dos valores das moedas

print("MOEDAS:")
print(num,"moeda(s) de R$ 1.00")
print(m50,"moeda(s) de R$ 0.50")
print(m25,"moeda(s) de R$ 0.25")
print(m10,"moeda(s) de R$ 0.10")
print(m5,"moeda(s) de R$ 0.05")
print(moedas,"moeda(s) de R$ 0.01")