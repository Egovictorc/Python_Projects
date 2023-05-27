from tkinter import Tk, Button, LEFT, TOP, RIGHT, BOTTOM


top = Tk()
red_btn = Button(top, text ="RED", fg="red")
red_btn.pack(side=LEFT)

blue_btn = Button(top, text ="Blue", fg="blue")
blue_btn.pack(side=TOP)

green_btn = Button(top, text ="Green", fg="green")
green_btn.pack(side=RIGHT)

black_btn = Button(top, text ="Black", fg="black")
black_btn.pack(side=BOTTOM)

top.mainloop()

