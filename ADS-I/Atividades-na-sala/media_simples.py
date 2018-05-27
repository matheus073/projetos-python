n1 = float(input("Digete a 1ª nota: "))
n2 = float(input("Digete a 2ª nota: "))
n3 = float(input("Digete a 3ª nota: "))

media = (n1+n2+n3)/3

if media < 7:
    print("Reprovado")
else:
    print("Aprovado")