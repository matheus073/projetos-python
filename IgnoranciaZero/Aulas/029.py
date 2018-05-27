num = float(int("Digete um numero: "))
lista = []
cont = 0
while num != -1:
    lista.append(num)
    num = float(int("Digete um numero: "))

for i in lista:
    if i % 2 == 0:
        print(i)

