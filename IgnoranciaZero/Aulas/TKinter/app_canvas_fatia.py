from tkinter import *

class Fatia(object):
    def __init__(self,i):

        self.font=("Verdana",20,"bold")

        self.x,self.y=50,50

        self.c=Canvas(i,width=300,height=300)
        self.c.pack()

        self.frame=Frame(i)
        self.frame.pack()

        self.c.create_oval((self.x,self.y),(self.x+200,self.y+200),fill="blue")

        self.l1=Label(self.frame,text="Fatiar",font=self.font,fg="blue")
        self.e=Entry(self.frame,fg="red",font=self.font,width=5)
        self.l2=Label(self.frame,text="%",font=self.font,fg="blue")
        self.b=Button(self.frame,text="Desenhar",font=self.font,command=self.fatiar)

        self.l1.pack(side=LEFT)
        self.e.pack(side=LEFT)
        self.l2.pack(side=LEFT)
        self.b.pack(side=LEFT)

        self.cont=0

    def fatiar(self):
        n=3.6*int(self.e.get())

        if n<self.cont:
            self.c.delete("arc")

        self.c.create_arc((self.x,self.y),(self.x+200,self.y+200),fill="orange",extent=n,tag="arc")
        self.cont=n

if __name__=="__main__":
    i=Tk()
    i["bg"]="#7767FF"
    Fatia(i)
    i.mainloop()
