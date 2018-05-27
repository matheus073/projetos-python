
from tkinter import *

janela=Tk()

def bt_click():
    lb["text"]=en.get();

en=Entry(janela)
en.place(x=100,y=100)

bt=Button(janela,widt=20,text="ok",command=bt_click)
bt.place(x=100,y=150)

lb=Label(janela,text="Label")
lb.place(x=100,y=200)
janela.geometry("300x300")
janela.mainloop()