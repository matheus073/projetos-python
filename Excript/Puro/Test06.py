#Função e metodos

def soma(x,y):
    total=x+y
    print("A soma de ",x,"+",y,"=",total)

soma(5,10)

#Argumentos posicionais VS Nomeada
def dado_pessoais(nome,idade,sexo):
    print("Nome = {}\nIdade = {}\nsexo = {}".format(nome,idade,sexo))

#dado_pessoais("Matheus",17,True)
dado_pessoais(idade=18,nome="matheus",sexo=True)

#funcois variaticar
def test01(*x):
    return print(x)

test01(1,3,45)