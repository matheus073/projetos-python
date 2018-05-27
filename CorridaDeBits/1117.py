cont = 0
while True:
    n = float(input())
    if 0<n<=10 :
        cont += 1
        if cont == 1:
            x = n
        else:
            x = (x+n)/2
            print("media = %.2f"%x)
            break
    else:
        print("nota invalida")