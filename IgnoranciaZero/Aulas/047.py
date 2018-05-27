periodo = input("Qual horario você estuda(M - Matutino, V - Vespertino, N - Noturno): ")

if periodo == "M" or periodo == "m":
    print("Bom dia!")
elif periodo == "V" or periodo == "v":
    print("Boa tarde!")
elif periodo == "N" or periodo == "n":
    print("Boa noite!")
else:
    print("Valor invalido")
