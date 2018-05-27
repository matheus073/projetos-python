n=int(input("Digete um numero n: "))
i=0

while i+(i+1)+(i+2)<n:
    i+=1

if i+(i+1)+(i+2)==n :
    print(n,"É perfeito")
else:
    print(n,"N é perfeito")