#from tkinter import Tk, Button, LEFT, TOP, RIGHT, BOTTOM
from tkinter import *

parent = Tk()
parent.geometry("300x200")

redbutton = Button(parent, text = "Red", fg = "red")
redbutton.pack( side = LEFT)
greenbutton = Button(parent, text = "Green", fg = "black")
greenbutton.pack( side = RIGHT )
bluebutton = Button(parent, text = "Blue", fg = "blue")
bluebutton.pack( side = TOP )
blackbutton = Button(parent, text = "Black", fg = "red")
blackbutton.pack( side = BOTTOM )

parent.mainloop()