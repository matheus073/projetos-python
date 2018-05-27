fatorial=int(input("Fatorial de: "))
print("%i! = " %fatorial, end="")

for i in range(fatorial,0,-1):
    if i==1 :
        print("%i"%i,end=" = %i"%fatorial)
        break
    print("%i" % (i), end=" * ")

    fatorial*=(i-1)