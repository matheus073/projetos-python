from tkinter import *

janela=Tk()


lb1=Label(janela,bg="blue",text="TOP")
lb1.pack(side=TOP,fill=X)

lb2=Label(janela,bg="green")
lb2.pack(side=RIGHT,fill=Y)

lb3=Label(janela,bg="green")
lb3.pack(side=LEFT,fill=Y)

lb4=Label(janela,bg="blue",text="BOTTOM")
lb4.pack(side=BOTTOM,fill=X)

janela.geometry("600x600")
janela.mainloop()