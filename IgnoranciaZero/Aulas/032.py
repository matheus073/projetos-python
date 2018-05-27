import random
meuJogo = []#[7, 9, 14, 23, 29, 50]


for x in range(6):
    jogo = int(input("digete o %iº numero: " % (x + 1)))
    meuJogo.append(jogo)

meuJogo.sort()

print("Seus numeros são:",meuJogo)

megaSena = list(range(1, 61))

n = int(input("Quantas tentativas deseja realizar: "))

for i in range(n):
    sorte = []
    cont = 0

    while sorte != meuJogo:
        megaSorte = megaSena.copy()
        sorte = []

        for j in range(6):
            numSonteado = random.choice(megaSorte)
            sorte.append(numSonteado)
            megaSorte.remove(numSonteado)

        sorte.sort()

        cont += 1

    print("Você ganharia com %i tentativas" % cont)
