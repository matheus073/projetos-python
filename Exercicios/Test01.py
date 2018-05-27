from  tkinter import *

janela=Tk()


for i in range(5):
    lb10 = Label(janela, bg="black")
    lb10.pack(side=TOP)

def lista():
    valor = ent1.get().split("-")
    pri=int(valor[0])
    seg=int(valor[1])
    lista_resultado=list(range(pri,seg+1))
    lb7["text"]=lista_resultado


lb1=Label(janela,text="Digite um numero para obter um lista(use o '-' para delimitar o intervalo)")
lb1.pack(side=TOP)
lb2=Label(janela,bg="black")
lb2.pack(side=TOP)
lb2=Label(janela,bg="black")
lb2.pack(side=TOP)


ent1=Entry(janela)
ent1.pack(side=TOP)


lb2=Label(janela,bg="black")
lb2.pack(side=TOP)

bt=Button(janela,text="Entrada",command=lista)
bt.pack(side=TOP)
lb2=Label(janela,bg="black")
lb2.pack(side=TOP)
lb7=Label(janela,text="A lista gerada foi:  ")
lb7.pack(side=TOP)

janela["bg"]="black"
janela.geometry("450x400")
janela.mainloop()