x = input()

x = x.split()
a,b,c,maior=int(x[0]),int(x[1]),int(x[2]),0

if a>=b and a>=c:
    maior = a
elif b>=a and b>=c:
    maior = b
else:
    maior = c

print("%i eh o maior"%maior)
