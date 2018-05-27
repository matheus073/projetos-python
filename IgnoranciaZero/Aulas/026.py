par=[]
impar  = []
for i in range(1,21):
    vetor = int(input("Digete numeros inteiros %i de 20: "%i))
    if vetor % 2 == 0:
        par.append(vetor)
    else:
        impar.append(vetor)

print("Lista de numeros pares: " ,par)
print("Lista de numeros impares: ",impar)
