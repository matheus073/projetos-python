n=int(input("Digete um numero menor que 10: "))
aux=n
i=0
dig=0

while aux!=0:
    dig=aux%10
    aux//=10
    i=dig+i*10

if n==i:
    print("são iguais")
else:
    print("n são iguais")