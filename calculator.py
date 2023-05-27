from tkinter import *

window = Tk()
window.title("NIIT Calculator")
window.resizable(width=False, height=False)

#window.iconbitmap('/path/to/ico/icon.ico')
icon = PhotoImage(file="calc.png")
window.iconphoto(True, icon)

# set window menu
menubar = Menu(window)
window.config(menu = menubar)
file = Menu(menubar, tearoff = 0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

menubar.add_cascade(label="File", menu=file)
menubar.add_command(label="Edit")
menubar.add_command(label="Help")

#**********************btn commands *************************
def enter_text(btn_text):
    expression = display_text["text"]
    #****************replace special operator characters **********************

# implement clear function

    # ***************** reject duplicate side decimal point ***************
    if(expression and "." in expression and btn_text == "."):
        return
    # ***************** do nothing, to implement later ***************
    elif btn_text == "C":
        display_text["text"] = ""
    elif btn_text == "CE":
        display_text["text"] = expression[0: len(expression)-1]
    elif btn_text == "DEL":
        pass
    # ***************** change sign on plus minus ***************
    elif btn_text == chr(177):
        display_result["text"] = -1 * display_result["text"]

    elif btn_text == "=":
        expression = expression.replace(chr(120), "*").replace(chr(247), "/")
        display_result["text"] = eval(expression)

        # clear expression
        #display_text["text"] = ""
    else:
        display_text["text"] = expression + btn_text


#********************************** calculator screens ********************************#
# screen frame to hold screens
# btn frame to hold buttons
btn_frame = Frame(window, borderwidth=3)
screen_frame = Frame(window, relief=RIDGE )

screen_frame.pack(fill=BOTH)
btn_frame.pack()


props = {
"relief": SUNKEN,
"borderwidth": 3,
"height": 3,
"font": ("arial", 24, "bold"),
    "width": 4,
    "height": 1
}

#*********************** display for entries ***********************
display_result = Label(screen_frame, justify=RIGHT, **props)
display_text = Label(screen_frame,  justify=RIGHT, **props )

display_text.pack(fill=BOTH)
display_result.pack(fill=BOTH)

calc_btns = {
    # ******************* row 1 btns **********************
    (0,0): "CE",
    (0,1): "C",
    (0,2): "DEL",
    (0,3): chr(247),

    # ******************* row 2 btns **********************
    (1,0): "7",
    (1,1): "8",
    (1,2): "9",
    (1,3): chr(120),

    # ******************* row 3 btns **********************
    (2,0): "4",
    (2,1): "5",
    (2,2): "6",
    (2,3): "-",

    # ******************* row 4 btns **********************
    (3,0): "1",
    (3,1): "2",
    (3,2): "3",
    (3,3): "+",

    # ******************* row 5 btns **********************
    (4,0): chr(177),
    (4,1): "0",
    (4,2): ".",
    (4,3): "=",
}


for k, v in calc_btns.items():
    btn = Button(btn_frame, text=v, **props, command= lambda x= v: enter_text(x))
    # ***************** change btn numbers background colors *******************
    if(k[0] == 0 or k[0] == 4 or k[1] == 3):
        btn["bg"] = "burlywood"
    btn.grid(row=k[0], column=k[1])



window.mainloop()
