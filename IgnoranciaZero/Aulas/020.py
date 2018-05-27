a=float(input("Degete o valor de A: "))
if a!=0:

    b=float(input("Degete o valor de B: "))
    c=float(input("Degete o valor de C: "))
    print()
    delta=(b**2)-4*a*c

    if delta==0:
        raiz=(-b+(delta**(1/2)))/2*a
        print("O delta = 0, só possui uma raiz real: %.1g"%raiz)

    elif delta<0:
        print("O delta = 0, não possui raiz real\nEncerrando o programa")

    else:
        raiz1 = (-b + (delta ** (1 / 2))) / 2 * a
        raiz2 = (-b - (delta ** (1 / 2))) / 2 * a

        print("O delta possui duas raizes reais: %.1g e %.1g" %( raiz1,raiz2))



else:
    print("Não é do segundo grau")
