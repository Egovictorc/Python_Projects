from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(height=False, width=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=("arial", 20, "bold"), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad= "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=("arial", 20, "bold"), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i+=1

#==========================#==================#=============
btnClear = Button(calc, text=chr(67), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=0)
btnAllClear = Button(calc, text=chr(67)+chr(69), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue")
btnAllClear.grid(row=1, column=1)
btnSq = Button(calc, text="r", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=2, pady=1)
btnAdd = Button(calc, text="+", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=1, column=3, pady=1)
btnSub = Button(calc, text="-", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=2, column=3, pady=1)
btnMul = Button(calc, text="x", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=3, column=3, pady=1)
btnDiv = Button(calc, text=chr(247), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=4, column=3, pady=1)
btnZero = Button(calc, text="0", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=0, pady=1)
btnDot = Button(calc, text=".", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=1, pady=1)
btnPM = Button(calc, text=chr(177), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=2, pady=1)
btnEquals = Button(calc, text="=", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="powder blue").grid(row=5, column=3, pady=1)

#=================Menu and function ==============
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you wish to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(height=False, width=False)
    root.geometry("944x568+0+0")

def Standard():
    root.resizable(height=False, width=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=iExit)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Updates")
helpmenu.add_command(label= "About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.configure(menu=menubar)

root.mainloop()