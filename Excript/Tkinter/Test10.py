from tkinter import *

janela=Tk()

lb1=Label(janela,text="Label1",bg="yellow")
lb1.pack(side=TOP,fill=BOTH,expand=1)


lb2=Label(janela,text="Label2",bg="green")
lb2.pack(side=TOP,fill=BOTH,expand=1)


lb3=Label(janela,text="Label3",bg="yellow")
lb3.pack(side=TOP,fill=BOTH,expand=1)


lb4=Label(janela,text="Label4",bg="green")
lb4.pack(side=TOP,fill=BOTH,expand=1)


janela.geometry("500x500")
janela.mainloop()