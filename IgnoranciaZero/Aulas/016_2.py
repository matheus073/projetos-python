n=int(input("Digete o numeros de segmento: "))
pro=0
ant=int(input("Degete o numero 1º: "))
seg=cont=1

while cont<n:
    pro=int(input("Digete o numero %iº: "%(cont+1)))
    cont+=1
    if ant!=pro:
        seg+=1
    ant=pro

print("Tem %i de segmentos"%seg)