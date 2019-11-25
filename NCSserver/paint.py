#!/usr/bin/python3

__author__ = 'Michele Penzo'
__version__ = '1.0'

from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    default_pen_size=2.0
    default_color='black'

    def __init__(self):
        self.root=Tk()

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)
        
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None

        self.line_width = self.default_pen_size
        self.color = self.default_color
        
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
    
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.default_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x=None
        self.old_y=None


if __name__ == '__main__':
    Paint()