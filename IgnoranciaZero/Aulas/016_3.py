cont=1000

while cont<10000:

    if ((cont%100)+(cont//100))**2==cont:
        print(cont)
    cont+=1