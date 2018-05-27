j=7

for i in range(1,10,2):
    cont=0
    while cont<=2:
       
        print("I=%i J=%i"%(i,j))  
        cont+=1
        j-=1
        if cont == 3:
            j+=5