from tkinter import *

CANVASX=400
CANVASY=400

class SPFC(object):
    def __init__(self, i):
        self.c = Canvas(i,width=CANVASX,height=CANVASY)
        self.c.pack()
        self.c.create_rectangle((150,150),(270,200),fill="white")
        self.c.create_rectangle((160,160),(260,195),fill="black")
        self.c.create_text((210,178),font=("Verdana","20"),text="SPFC",fill="white")
        self.c.create_polygon((150,200),(270,200),(210,320),fill="white")
        self.c.create_polygon((160,210),(202,210),(207,310),fill="red")
        self.c.create_polygon((213,210),(255,210),(213,310))


if __name__ == '__main__':
    i = Tk()
    i["bg"]="blue"
    SPFC(i)
    i.mainloop()
