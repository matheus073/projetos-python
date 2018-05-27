lista=[]
print("Comandos:\n0: Para sair\n1: Para adicionar\n2: Para remover\n3: Para ver a lista\n4: Para alterar\n5: Para limpar a lista\n6: Para ordenar a lisra")
comando=int(input("Digite um comando: "))
verificar='null'

while(comando!=0):

    if(comando==1):#adicionar
        print("Para sair digite 'sair'")
        while(verificar!="sair"):
            verificar=input("Informe o item da lista: ")
            if(verificar!="sair"):
                lista.append(verificar)
                #lista=lista+[verificar]
                #lista.insert(-1,verificar)

    elif(comando==2):#remover
        remover=int(input("Para remover digete o numero da posição que o ietm está: "))
        del(lista[remover-1])

    elif(comando==3):
        #Ver lista
        print(lista)

    elif(comando==4):
        verificar=int(input("Digite a posição a ser mudada: "))-1
        palavra_certa=input("Digite a palavra o nome certo: ")
        lista[verificar]=palavra_certa

    elif(comando==5):
        sim_ou_nao=int(input("Tem certeza que quer lipmar a lista(sim='1')?\n"))
        resultado=lista.clear() if sim_ou_nao==1 else print("Lista não excluida")

    elif(comando==6):
        #ordenar a lista
        lista.sort()


    else:
        print("Comando não existe")
    comando = int(input("Digite outro comando: "))