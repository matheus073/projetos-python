eleitores=int(input("Digete a quantidade de eleitores: "))
candidato1=candidato2=candidato3=0
resultado=0

for i in range(eleitores):
    resultado=int(input("Digete o numero do candidato (1, 2 ou 3): "))
    if resultado==1:
        candidato1+=1
    elif resultado==2:
        candidato2+=1
    elif resultado==3:
        candidato3+=1
    else:
        print("Voto nulo")

print("\n\nRESULTADO DOS VOTOS:\n1º candidato ficou com %i votos\n2º candidato ficou com %i votos\n3º candidato ficou com %i votos"%(candidato1,candidato2,candidato3))