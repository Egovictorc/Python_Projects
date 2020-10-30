from tkinter import *

props = {
    "font": ("arial", 20, "bold")
}

btn_props = {
    "width": 5,
    "height": 2,
    "borderwidth": 2,
    "relief": SUNKEN,
    "borderwidth": 5,
    **props
}

lbl_props = {
    "bg": "burlywood",
    "relief": SUNKEN,
    "borderwidth": 15,
    "padx": 10,
    "pady":10,
    **props
}

def calculator():
    """ our standard calculator"""
    window = Tk()
    window.title("Standard Calculator")

    # ********************* frames *********************************#
    frm_screen = Frame(window)
    frm_btn = Frame(window)
    frm_screen.pack(fill=BOTH)
    frm_btn.pack(fill=BOTH)

    #******************************* labels **********************#
    lbl_history = Label(frm_screen, text="", **lbl_props)
    lbl_input = Label(frm_screen, text="", **lbl_props)
    lbl_history.pack(fill=BOTH)
    lbl_input.pack(fill=BOTH)

    #**************************** initial values *******************#
    operator = ""
    lbl_history["text"] = ""
    lbl_input["text"] = ""
    result = 0

    #**************************** btns ************************#
    num_pad = "789456123"
    opr_pad = "x-+"
    bottom_btns = ["+/-", "0", ".", "=" ]
    top_btns = ["CE", "C", "d","/"]
    begin, end = 0, 3
    col = 0

    # ****************************top btns ************************#
    for i in range(0, len(top_btns)):
        btn = Button(frm_btn, text=top_btns[i], **btn_props, bg="burlywood")
        btn.grid(column=i, row=0)

    # ***************************number btns ***********************#
    for row in range(1, 4):
        for j in range(begin, end):
            btn = Button(frm_btn, text=num_pad[j], **btn_props, command= lambda x= num_pad[j]: num_handler(x))
            btn.grid(column=col, row=row)
            col +=1
            #********************* opr btns **********************#
        btn_opr = Button(frm_btn, text=opr_pad[row-1], **btn_props, bg="burlywood",
                         command= lambda x = opr_pad[row-1]: opr_handler(x))
        btn_opr.grid(column=3, row=row)
        begin, end = end, end + 3
        col = 0

    #*************************** bottom operator btns ********************#
    plus_minus = Button(frm_btn, text="+/-", **btn_props, bg="burlywood", command=lambda: num_handler("+/-"))
    plus_minus.grid(row=4, column=0)
    btn_zero = Button(frm_btn, text="0", **btn_props, command=lambda : num_handler("0"))
    btn_zero.grid(row=4, column=1)
    btn_dot = Button(frm_btn, text=".", **btn_props, command= lambda : dot_handler())
    btn_dot.grid(row=4, column=2)
    btn_equals = Button(frm_btn, text="=", **btn_props, bg="burlywood", command= lambda : dot_handler())
    btn_equals.grid(row=4, column=3)

    # for i in range(0, len(bottom_btns)):
    #     if i == 1 or i == 2:
    #         btn = Button(frm_btn, text=bottom_btns[i], **btn_props, command= lambda x = bottom_btns[i]: num_handler(x))
    #         btn.grid(row=4, column=i)
    #         continue
    #     btn = Button(frm_btn, text=bottom_btns[i], **btn_props, bg="burlywood")
    #     btn.grid(row=4, column=i)

    #*********************** function number handler **********************#
    def num_handler(btn_text):
        text = lbl_input["text"]
        if not text:
            lbl_input["text"] = btn_text
        else:
            lbl_input["text"] = text + btn_text

    # *********************** function dot handler **********************#
    def opr_handler(btn_text):
        input_ = lbl_input["text"]
        history = lbl_history["text"]

        if not (input or operator):
            return
        elif history:
            lbl_history["text"] = history + input_
        else:
            lbl_history["text"] = input_

    def dot_handler():
        xyz = lbl_history["text"]
        text = lbl_input["text"]
        if "." in text:
            return
        else:
            num_handler(".")


    window.mainloop()

calculator()
