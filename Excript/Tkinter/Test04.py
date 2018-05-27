from tkinter import *

def bt_clicado():

    lb["text"]="FUNCIONOL!!!"



janela=Tk()

janela.geometry("800x400")
janela["bg"]="#033453"

bt=Button(janela,width=20,text="ok",command=bt_clicado)
bt.place(x=100,y=155)

lb=Label(janela,text="Text")
lb.place(x=100,y=200)



janela.mainloop()