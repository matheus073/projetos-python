n = input().split()

n.sort()

a,b,c = float(n[0]),float(n[1]),float(n[2])

delta = (b**2) - (4*a*c)

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    r1 = (-b + (delta**0.5))/(2*a)
    r2 = (-b - (delta**0.5))/(2*a)
    
    print("R1 = %.5f"%r1)
    print('R2 = %.5f'%r2)

