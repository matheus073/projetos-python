print("Informe um valor entre 1 e 23 ou 0 para sair")

numeroDoJogador = int(input("Numero do jogador: "))
votos = []

while numeroDoJogador != 0:
    if 1 <= numeroDoJogador <= 23:
        votos.append(numeroDoJogador)
    print(votos)
    numeroDoJogador = int(input("Numero do jogador: "))

print("\nResultado da votação:\n")
print("foram computados %i votos\n" % (len(votos)))

melhorJogador = 1
porcentagemDoMelhorJogador = 0
pontuacaoDoMelhorJogador = 1
for i in range(1,24):
    votoEmI = votos.count(i)
    porcentagem = 100 * votoEmI / len(votos)
    if votoEmI > 0:
        print("%4.i             %4.i          %.1f%%" % (i, votoEmI, porcentagem))

    if votoEmI > melhorJogador:
        melhorJogador = votoEmI
        pontuacaoDoMelhorJogador = i
        porcentagemDoMelhorJogador = porcentagem

print("O melhor jogador foi o número %i, com %i votos, correspondendo a %.1f%% do total de votos." % (pontuacaoDoMelhorJogador, melhorJogador, porcentagemDoMelhorJogador))
