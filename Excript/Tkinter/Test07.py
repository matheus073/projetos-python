from tkinter import *

janela=Tk()

def bt_click():
    num1 = en1.get()
    num2 = en2.get()
    if(num1.isnumeric() and num2.isnumeric()):

        lb["text"]=int(num1)+int(num2)

    else:
        lb["text"]="Valores invalidos"

lb_info=Label(janela,text="Informe 2 valores inteiros para serem somados")
lb_info.place(x=30,y=50)
lb_info["bg"]="#00ffc3"

en1=Entry(janela)
en1.place(x=100,y=100)

en2=Entry(janela)
en2.place(x=100,y=130)

bt=Button(janela,width=17,text="SOMA",command=bt_click)
bt.place(x=100,y=160)

lb=Label(janela,text="Soma")
lb.place(x=100,y=200)



janela.geometry("300x300")
janela["bg"]="#00ffc3"
janela.mainloop()