num = input()

num = num.split()
a,b,c=float(num[0]),float(num[1]),float(num[2])

triangulo_retangulo = (a*c)/2
circulo = (c**2)*3.14159
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

print("TRIANGULO: %.3f"%triangulo_retangulo)
print("CIRCULO: %.3f"%circulo)
print("TRAPEZIO: %.3f"%trapezio)
print("QUADRADO: %.3f"%quadrado)
print("RETANGULO: %.3f"%retangulo)