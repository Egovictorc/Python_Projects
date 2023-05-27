from tkinter import *

parent = Tk()
#parent.geometry("300x200")

name = Label(parent,text = "Name")
name.grid(row = 0, column = 0)
e1 = Entry(parent, width=70)
e1.grid(row = 0, column = 1)
password = Label(parent,text = "Password")
password.grid(row = 1, column = 0)
e2 = Entry(parent, width=70)
e2.grid(row = 1, column = 1)
submit = Button(parent, text = "Submit", bg="red")
submit.grid(row = 2, column = 0, columnspan=2, sticky="news")
parent.mainloop()