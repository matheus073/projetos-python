from tkinter import *

class Carinha(object):
    def __init__(self,i):
        self.root=i
        self.c=Canvas(i,width=200,height=200,bg="#827CFF")
        self.c.pack()

        self.c.create_oval((85,85),(115,115),fill="yellow",tag="cara")
        self.c.create_oval((90,92),(95,97),fill='blue',tag="cara")
        self.c.create_oval((110,92),(105,97),fill='blue',tag="cara")
        self.c.create_line((90,105),(100,110),(110,105),fill="green",tag="cara")

        self.b=Button(i,text='Start',command=self.Mover)
        self.b.pack()

        self.vx = 10
        self.vy = 10
        self.x = 5
        self.y = 3


    def Mover(self):
        self.c.move('cara',self.x,self.y)
        self.vy+=self.y
        self.vx+=self.x

        if self.vx>=95 or self.vx<=-70:
            self.x*=-1
        if self.vy>=95 or self.vy<=-70:
            self.y*=-1

        self.root.after(30,self.Mover)



if __name__=="__main__":

    i=Tk()

    Carinha(i)

    i.mainloop()