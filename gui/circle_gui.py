#!/usr/bin/python3

__author__ = 'Michele Penzo'

from tkinter import *
from tkinter.colorchooser import askcolor
import pyautogui
from math import sqrt
from time import sleep

class Paint(object):

    # default parameters
    default_pen_size=4.0
    default_color='black'
    
    # -------------------
    # ---- max delay ----
    MAX_DELAY = 0.3

    x, y = 960,500     # starting coordinate of circle --> not the center of monitor
    radius = 350 - default_pen_size

    # whiteboard
    def __init__(self):
        self.root=Tk()
        self.root.title('NCS Server')
    
        # the new cursor
        self.root.config(cursor='arrow red')

        # get width and height
        _width=self.root.winfo_screenwidth()
        _height=self.root.winfo_screenheight()
        
        # canvas
        self.c = Canvas(self.root, bg='white', width=_width, height=_height)
        self.c.grid(row=1, columnspan=5)

        # distance labele
        self.label = Label(self.root, text='Errore --->   ', font=("Helvetica", 16))
        self.label.grid(sticky = E, row=0, column=0) 
        
        # correction error printed here
        self.label_error = Label(self.root, text='', font=("Helvetica", 16))
        self.label_error.grid(sticky = W, row=0, column=1) 

        # exit button
        self.exit_button = Button(self.root, text='Chiudi', font=("Helvetica", 16), command=exit)
        self.exit_button.grid(sticky = W, row=0, column=2) 

        # getting the coordinates 
        x1, y1 ,x2 ,y2 = self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius
        self.c.create_oval(x1, y1, x2, y2, outline="#3427a3", fill="#add4d9", width=self.default_pen_size)
        
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

    
    # method for writing on whiteboard
    def paint(self, event):
        
        if self.old_x and self.old_y:
            sleep( self.MAX_DELAY )    # milliseconds
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.default_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)

        self.old_x = event.x
        self.old_y = event.y
        
        # calculating distance from center
        distance = sqrt( (self.old_x - self.x)**2 + (self.old_y - self.y)**2 ) - self.radius

        self.label_error['text'] = round(distance,2)

    # reset value
    def reset(self, event):
        self.old_x=None
        self.old_y=None


if __name__ == '__main__':
    Paint()