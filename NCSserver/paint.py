#!/usr/bin/python3

__author__ = 'Michele Penzo'

from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):

    # parametri definiti di default
    default_pen_size=2.0
    default_color='black'

    # creo il quadrato bianco dove posso disegnare
    def __init__(self):
        self.root=Tk()
        self.root.title('NCS Server')
        
        '''
        _width=self.root.winfo_screenwidth()
        _height=self.root.winfo_screenheight()
        '''
        _width=600
        _height=800

        self.c = Canvas(self.root, bg='white', width=_width, height=_height)
        self.c.grid(row=1, columnspan=5)
        
        self.setup()
        
        self.root.mainloop()

    # setta i valori di base come colore e tratto della linea
    def setup(self):
        self.old_x = None
        self.old_y = None

        self.line_width = self.default_pen_size
        self.color = self.default_color
        
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    # metodo che uso per scrivere all'interno del quadrato
    def paint(self, event):
    
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.default_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y

    # mantiene i valori della x e y precedente
    def reset(self, event):
        self.old_x=None
        self.old_y=None
    

if __name__ == '__main__':
    Paint()