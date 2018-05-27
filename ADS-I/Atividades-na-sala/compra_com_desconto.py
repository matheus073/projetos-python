x = float(input("Preço: "))
y = int(input("Quantidade: "))

valor = x*y

if y > 7:
    valor *= 0.9

print("Total a pagar:",valor)
