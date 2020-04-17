#!/usr/bin/python3

__author__ = 'Michele Penzo'

from tkinter import *
from tkinter.colorchooser import askcolor
import random
class Paint(object):

    # default parameters
    default_pen_size=4.0
    default_color='black'

    # whiteboard
    def __init__(self):
        self.root=Tk()
        self.root.title('NCS Server')
        
        
        _width=self.root.winfo_screenwidth()
        _height=self.root.winfo_screenheight()

        self.c = Canvas(self.root, bg='white', width=_width, height=_height)
        self.c.grid(row=1, columnspan=5)

        self.label_error = Label(self.root, text='Valore error correction -->    ', font=("Helvetica", 16))
        self.label_error.grid(sticky = E, row=0, column=0) 
        
        # correction error printed here
        self.label_error = Label(self.root, text='', font=("Helvetica", 16))
        self.label_error.grid(sticky = W, row=0, column=1) 

        # TODO center oval con disegno con x1 e y1
        pos_y, pos_x =  _width/2, _height/2

        self.c.create_oval(pos_x-500, pos_y-500, pos_x, pos_y, outline="#ff0000", fill="#1fba32", width=2)
        
        self.setup()
        
        self.root.mainloop()

    # set base values
    def setup(self):
        self.old_x = None
        self.old_y = None

        self.line_width = self.default_pen_size
        self.color = self.default_color
        
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    # method for writing inside whiteboard
    def paint(self, event):
    
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.default_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y

        # calculating error correction value
        self.label_error['text'] = random.randint(0,5)

    # reset value
    def reset(self, event):
        self.old_x=None
        self.old_y=None

if __name__ == '__main__':
    Paint()