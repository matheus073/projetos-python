num=input()

t=num.split()

tri=float(t[0]),float(t[1]),float(t[2])
tri=list(tri)
tri.sort()

c,b,a=tri[0],tri[1],tri[2]
if a>=b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2==b**2+c**2:
        print("TRIANGULO RETANGULO")
    if a**2>b**2+c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2<b**2+c**2:
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif a==b or a==c or b==c:
        print("TRIANGULO ISOSCELES")    