from tkinter import *
from functools import partial

janela=Tk()

def bt_click(botao):
    print(botao["text"])

bt1=Button(janela,width=20,text="botao 1")
bt1.place(x=100,y=100)
bt1["bg"]="#ff0000"
bt1["command"]=partial(bt_click,bt1)

bt2=Button(janela,width=20,text="botao 2")
bt2.place(x=100,y=130)
bt2["bg"]="#ff0000"
bt2["command"]=partial(bt_click,bt2)



janela["bg"]="gray"
janela.geometry("300x300")
janela.mainloop()