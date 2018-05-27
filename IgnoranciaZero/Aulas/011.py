numero=int(input("Digete o numero: "))

centena=numero//100
dezena=(-(centena*100)+numero)//10
unidade=(-(centena*100+dezena*10)+numero)

if (centena!=0 and dezena!=0 and unidade!=0):
    if(centena==1 and dezena==1 and unidade==1):
        print(centena,"centena,",dezena,"dezena e",unidade,"unidade")

    elif (centena>1 and dezena==1 and unidade==1):
        print(centena, "centenas,", dezena, "dezena e", unidade, "unidade")

    elif (centena==1 and dezena>1 and unidade==1):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidade")

    elif (centena==1 and dezena==1 and unidade>1):
        print(centena, "centenas,", dezena, "dezena e", unidade, "unidades")

    elif (centena>1 and dezena>1 and unidade==1):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidade")

    elif (centena>1 and dezena==1 and unidade>1):
        print(centena, "centenas,", dezena, "dezena e", unidade, "unidades")

    elif (centena==1 and dezena>1 and unidade>1):
        print(centena, "centena,", dezena, "dezenas e", unidade, "unidades")

    elif (centena>1 and dezena>1 and unidade>1):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidades")

elif (centena==0 and dezena!=0 and unidade!=0):
    if(dezena==1 and unidade==1):
        print(dezena,"dezena e",unidade,"unidade")

    elif (dezena==1 and unidade==1):
        print(dezena, "dezena e", unidade, "unidade")

    elif (dezena>1 and unidade==1):
        print(dezena, "dezenas e", unidade, "unidade")

    elif (dezena==1 and unidade>1):
        print(dezena, "dezena e", unidade, "unidades")

    elif (dezena>1 and unidade==1):
        print(dezena, "dezenas e", unidade, "unidade")

    elif (dezena==1 and unidade>1):
        print(dezena, "dezena e", unidade, "unidades")

    elif (dezena>1 and unidade>1):
        print(dezena, "dezenas e", unidade, "unidades")

    else:
        print(dezena, "dezenas e", unidade, "unidades")

elif (centena!=0 and dezena==0 and unidade!=0):
    if(centena==1  and unidade==1):
        print(centena,"centena e",unidade,"unidade")

    elif (centena>1  and unidade==1):
        print(centena, "centenas e", unidade, "unidade")

    elif (centena==1  and unidade==1):
        print(centena, "centenas e", unidade, "unidade")

    elif (centena==1  and unidade>1):
        print(centena, "centenas e", unidade, "unidades")

    elif (centena>1 and unidade==1):
        print(centena, "centenas e", unidade, "unidade")

    elif (centena>1 and unidade>1):
        print(centena, "centenas e", unidade, "unidades")

    elif (centena==1 and unidade>1):
        print(centena, "centena e", unidade, "unidades")

    elif (centena>1 and unidade>1):
        print(centena, "centenas e", unidade, "unidades")

elif (centena!=0 and dezena!=0 and unidade==0):
    if(centena==1 and dezena==1):
        print(centena,"centena e",dezena," dezena")

    elif (centena>1 and dezena==1 ):
        print(centena, "centenas e", dezena, "dezena")

    elif (centena==1 and dezena>1):
        print(centena, "centenas e", dezena, "dezenas")

    elif (centena==1 and dezena==1):
        print(centena, "centenas e", dezena, "dezena ")

    elif (centena>1 and dezena>1 ):
        print(centena, "centenas e", dezena, "dezenas ")

    elif (centena>1 and dezena==1):
        print(centena, "centenas e", dezena, "dezena ")

    elif (centena==1 and dezena>1):
        print(centena, "centena e", dezena, "dezenas ")

    elif (centena>1 and dezena>1):
        print(centena, "centenas e", dezena, "dezenas ")

elif (centena==0 and dezena==0 and unidade!=0):
    if(unidade==1):
        print(unidade,"unidade")

    else:
        print(unidade, "unidades")

elif (centena==0 and dezena!=0 and unidade==0):
    if(dezena==1):
        print(dezena,", dezena")

    else:
        print(dezena, ", dezenas")

elif (centena!=0 and dezena==0 and unidade==0):
    if(centena==1):
        print(centena,"centena")

    else:
        print(centena, "centenas")