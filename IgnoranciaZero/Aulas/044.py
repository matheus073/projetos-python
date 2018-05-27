atleta=input("Atleta: ")
notas=[]
media=0

for i in range(7):
    notas.append(float(input("Notas: ")))
notas.sort()
melhor=notas[6]
pior=notas[0]
for m in range(1,6):
    media+=notas[m]
media/=5

print("\n\nResultado final:\nAtleta: %s\nMelhor nota: %2g\nPior nora: %2g\nMédia: %2g"%(atleta,melhor,pior,media))