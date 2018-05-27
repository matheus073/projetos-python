from tkinter import *

class Mario(object):
    def __init__(self,i):

        self.root=i

        self.CarregaImagem()

        self.c=Canvas(i,width=200,height=100,bg="black")
        self.c.pack()

        self.b=Button(i,text="Start",command=self.IniciarJogo)
        self.b.focus_force()
        self.b.pack()

        self.c.bind("<Left>",self.Esquerdo)
        self.c.bind("<Right>",self.Direito)


        self.cont_left=0
        self.cont_right=0
        self.passos=100
        self.verificar=True
    def IniciarJogo(self):
        if self.verificar:
            self.c.focus_force()
            self.c.create_image((100,70),image=self.imagem_direita[0])

    def Esquerdo(self,esp):
        self.verificar=False
        self.c.delete(ALL)
        self.cont_left+=1
        if self.passos>=20:
            self.passos-=5
        self.c.create_image(self.passos,70,image=self.imagem_esquerda[self.cont_left])
        if self.cont_left==len(self.imagem_esquerda)-1:
            self.cont_left=0

    def Direito(self,esp):
        self.verificar=False
        self.c.delete(ALL)
        self.c.create_image(self.passos,70,image=self.imagem_direita[self.cont_right])
        self.cont_right+=1

        if self.passos<180:
            self.passos+=10

        if self.cont_right==len(self.imagem_direita)-1:
            self.cont_right=0

    def CarregaImagem(self):
        self.imagem_direita=[]
        self.imagem_esquerda=[]

        for i in range(1,5):
            self.imagem_direita.append(PhotoImage(file="Imagens/mario/mario_%i.ppm"%i))

        for i in range(1,5):
            self.imagem_esquerda.append(PhotoImage(file="Imagens/mario/mario_l%i.ppm"%i))



if __name__=="__main__":
    i=Tk()
    i.resizable(False,False)
    i["bg"]="blue"
    i.title("Mario")
    Mario(i)
    i.mainloop()