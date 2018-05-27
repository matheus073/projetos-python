i=int(input("Digete o valor de i: "))
j=int((input("Digete o valor de j: ")))

if i<j:
    for x in range(1,i+1):
        if i%x==0 and j%x==0:
            print(x)

elif j<i:
    for x in range(1,j+1):
        if i%x==0 and j%x==0:
            print(x)

else:
    for x in range(1,i+1):
        if i%x==0 and j%x==0:
            print(x)