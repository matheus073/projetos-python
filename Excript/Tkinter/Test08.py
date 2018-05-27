

from tkinter import *

janela=Tk()

lb1=Label(janela,text="Top")
lb1.pack(side=TOP)

lb2=Label(janela,text="Bottom")
lb2.pack(side=BOTTOM)

lb3=Label(janela,text="Right")
lb3.pack(side=RIGHT)

lb4=Label(janela,text="Left")
lb4.pack(side=LEFT)


janela["bg"]="black"
janela.geometry("400x400")
janela.mainloop()