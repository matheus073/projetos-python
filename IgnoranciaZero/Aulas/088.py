from tkinter import *

i=Tk()

i.title("Login")

ususario_label=Label(i,text="Usuario")
ususario_label.pack()

usuario_entrada=Entry(i)
usuario_entrada.pack()

senha_label=Label(i,text="Senha")
senha_label.pack()

senha_entry=Entry(i)
senha_entry.pack()

button=Button(i,text="Entrar")
button.pack()


i.mainloop()