
from tkinter import *

class Linhas(object):
    def __init__(self,i):
        self.canvas=Canvas(i,width=400, height=400,cursor="target",bd=5)
        self.canvas.pack()

        self.y,self.x=200,200



        self.frame=Frame(i)
        self.frame.pack()
        configs={"fg":"darkblue","bg":"ghostwhite",'relief':GROOVE, 'width':11,'font':('Verdana','8','bold')}


        self.b1 = Button(self.frame, configs, text='Esquerda', command=self.left)
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.frame, configs, text='Para cima', command=self.up)
        self.b2.pack(side=LEFT)

        self.b3 = Button(self.frame, configs, text='Para baixo', command=self.down)
        self.b3.pack(side=LEFT)

        self.b4 = Button(self.frame, configs, text='Direita', command=self.right)
        self.b4.pack(side=LEFT)


    def left(self):
        x1=self.x-10
        self.canvas.create_line(self.x,self.y,x1,self.y,fill="blue")
        self.x=x1

    def up(self):
        y1 = self.y - 10
        self.canvas.create_line(self.x, self.y, self.x, y1, fill="Black")
        self.y = y1

    def down(self):
        y1 = self.y + 10
        self.canvas.create_line(self.x, self.y, self.x, y1, fill="pink")
        self.y = y1

    def right(self):
        x1 = self.x + 10
        self.canvas.create_line(self.x, self.y, x1, self.y, fill="green")
        self.x = x1



if __name__=='__main__':
    i=Tk()

    Linhas(i)

    i.mainloop()
