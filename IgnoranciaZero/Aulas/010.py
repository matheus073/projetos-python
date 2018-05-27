saque=int(input("Valor do saque: "))

if 10<=saque<=600:

    cem=saque//100
    saque%=100

    cinquenta=saque//50
    saque%=50

    dez=saque//10
    saque%=10

    cinco=saque//5
    saque%=5

    um=saque//1
    saque%=1

if cem>0:
    print(cem,"notas de 100")

if cinquenta>0:
    print(cinquenta,"notas de 50")

if dez > 0:
    print(dez, "notas de 10")

if cinco>0:
    print(cinco,"notas de 5")

if um>0:
    print(um,"notas de 1")

