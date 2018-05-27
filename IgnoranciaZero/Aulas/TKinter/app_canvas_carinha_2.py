from tkinter import *

class Carinha2(object):
    def __init__(self,i):
        self.c=Canvas(i,width=200,height=200,bg="#827CFF")
        self.c.focus_force()
        self.c.pack()

        self.c.create_oval((85,85),(115,115),fill="yellow",tag="cara")
        self.c.create_oval((90,92),(95,97),fill='blue',tag="cara")
        self.c.create_oval((110,92),(105,97),fill='blue',tag="cara")
        self.c.create_line((90,105),(100,110),(110,105),fill="green",tag="cara")

        self.cima=self.c.bind("<Up>",self.Up)
        self.baixo=self.c.bind("<Down>",self.Down)
        self.esquerda=self.c.bind("<Left>",self.Left)
        self.direita=self.c.bind("<Right>",self.Right)

    def Up(self,exp):
        self.c.move('cara',0,-5)
    def Left(self,exp):
        self.c.move("cara",-5,0)
    def Right(self,exp):
        self.c.move("cara",5,0)
    def Down(self,exp):
        self.c.move("cara",0,5)

if __name__=="__main__":

    i=Tk()

    Carinha2(i)

    i.mainloop()