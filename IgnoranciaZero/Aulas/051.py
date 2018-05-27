total=0
def main():
    global total
    lista=transformarTxtEmLista("usuarios.txt")
    memoriaOcupada(lista)

    for i in range(len(lista)):
        total+=lista[i][1]

    gerarDocumento(lista,total)



def memoriaOcupada(tamnho):
    for i in range(len(tamnho)):
        tamnho[i][1] = float(tamnho[i][1])/(1024**2)

def transformarTxtEmLista(documento):
    arquivo = open(documento)
    linha=arquivo.readline()
    usuario=[]

    while linha!='':
        separar=linha.split()
        usuario.append(separar)

        linha=arquivo.readline()

    arquivo.close()
    return usuario

def porcentagem(usuario, espacoTotal):
    porc=[]
    for i in usuario:
        porc.append(100 * i[1] / espacoTotal)
    return porc

def espacos(num):
    cont=[]
    for i in str(num):
        cont.append(i)

    return cont



def gerarDocumento(usuarios,espacoTotal):

    arquivo=open("Relatorio.txt","w")
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo.write(65*"-"+"\n")
    arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

    porc=porcentagem(usuarios,espacoTotal)




    for i in range(len(usuarios)):
        a=str("%.2f"%(usuarios[i][1]))
        print((len(porc)+15)-len(a))

        arquivo.write("%i    %s       %.2f MB%s%.2f %%\n"%(i+1,usuarios[i][0]+(15 - len(usuarios[i][0]))*' ',usuarios[i][1],((len(porc)+15)-len(a))*' ',porc[i]))

    arquivo.write("\n\nEspaço total ocupado: %.2f\n"%total)
    arquivo.write("Espaço médio ocupado: %.2f"%(total/len(usuarios)))
    arquivo.close()






main()

