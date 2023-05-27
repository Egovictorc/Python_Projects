from tkinter import Tk, Button, Label, Menu, Frame, BOTH, SUNKEN

parent = Tk()
parent.title("NIIT Calculator") ## set gui title
#parent.geometry("300x400")
parent.resizable(width=False, height=False) ## enable / disable resizing
menubar = Menu()
file_menu = Menu(tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Open recent")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=parent.quit)
menubar.add_cascade(label="File", menu=file_menu)

#************** configure menubar ***************************
parent.config(menu=menubar)

##****************************** frames *********************
disp_frame = Frame(parent, height=30)
btn_frame = Frame(parent, height=65)

disp_frame.pack(fill=BOTH)
btn_frame.pack(fill=BOTH)

###***************** screen / displays ********************
display_props = {
"font": ("Arial",24, "bold")
}

display_expr = Label(disp_frame, bg="red", text="", **display_props )
display_result = Label(disp_frame, bg="green", text="12", **display_props )
display_expr.pack(fill=BOTH)
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

props = {
    "font": ("Arial", 26, "bold"),
    "width": 4,
    "relief": SUNKEN,
    "borderwidth": 4
}

def calc_fn(val):
    old_val = display_expr["text"]
    operators = [chr(177), chr(247), "+", "-", chr(120), "." ]
    if not old_val:
        old_val = val
        display_expr["text"] = val
    elif old_val[-1] in operators and val in operators:
        display_expr["text"] = old_val[0:-1] + val
    elif val == chr(177):
        display_result["text"] = -1 * display_result["text"]
    elif val == "=":
        without_unicodes = old_val.replace(chr(247), "/").replace(chr(120), "*")
        print(old_val)
        display_result["text"] = eval(without_unicodes)
    else:
        display_expr["text"] = old_val + val
    print(val)

for k, v in calc_btns.items():
    btn = Button(btn_frame, text=v, **props, command= lambda x=v: calc_fn(x))
    # ***************** change btn numbers background colors *******************

    if (k[0] == 0 or k[0] == 4 or k[1] == 3):
        btn["bg"] = "burlywood"
    btn.grid(row=k[0], column=k[1])

parent.mainloop()