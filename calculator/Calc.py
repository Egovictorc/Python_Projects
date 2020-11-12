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
    "pady": 10,
    **props
}

# **************************** initial values *******************#
result = 0
oper = ""
showed_result = False


def calculator():
    """ our standard calculator"""
    window = Tk()
    window.title("Standard Calculator")
    window.geometry("406x635")
    window.iconbitmap("icon1.ico")
    window.resizable(width=False, height=False)

    # ********************* frames *********************************#
    frm_screen = Frame(window)
    frm_btn = Frame(window)
    frm_screen.pack(fill=BOTH)
    frm_btn.pack(fill=BOTH)

    # ******************************* labels **********************#
    lbl_history = Label(frm_screen, text="", **lbl_props)
    lbl_input = Label(frm_screen, text="", **lbl_props)
    lbl_history.pack(fill=BOTH)
    lbl_input.pack(fill=BOTH)

    # **************************** initial values *******************#
    lbl_history["text"] = ""
    lbl_input["text"] = ""

    # *********************** function operator handler **********************#
    def opr_handler(btn_text):
        input_ = lbl_input["text"]
        global oper, result, showed_result
        if not input_:
            return
        elif input_ and not oper:
            oper = btn_text
            result = chk_dec(input_)
            hist_handler()
        else:
            compute()
            oper = btn_text
            hist_handler()
        showed_result = False

    # ************************* function check decimal *******************#
    def chk_dec(text):
        if "." in text:
            return float(text)
        return int(text)

    # *********************** function number handler **********************#
    def num_handler(btn_text):
        text = lbl_input["text"]
        if not text:
            lbl_input["text"] = btn_text
        else:
            lbl_input["text"] = text + btn_text

    # *********************** function compute **********************#
    def compute():
        num = lbl_input["text"]
        num = chk_dec(num)
        global result, oper
        if (oper == "+"):  # add
            result += num
        elif (oper == "-"):  # subtract
            result -= num
        elif (oper == "x"):  # multiply
            result *= num
        elif (oper == "/"):  # divide
            result /= num

    # *********************** function change sign handler **********************#
    def change_sign():
        text = lbl_input["text"]

        if not text:
            return
        text = lbl_input["text"]
        num = chk_dec(text)
        lbl_input["text"] = str(-1 * num)

    # *********************** function history handler **********************#
    def hist_handler():
        input_ = lbl_input["text"]
        history = lbl_history["text"]

        if not history or showed_result:
            lbl_history["text"] = input_ + oper
        else:
            lbl_history["text"] = history + input_ + oper
        lbl_input["text"] = ""

    # *********************** function dot handler **********************#
    def dot_handler():
        text = lbl_input["text"]
        if "." in text:
            return
        else:
            num_handler(".")

    # *********************** function result handler **********************#
    def display_result():
        global oper, showed_result
        compute()
        oper = ""
        history = lbl_history["text"]
        input_ = lbl_input["text"]
        result = remove_zero()
        # ****************** change history *****************************#
        lbl_history["text"] = f"{history}{input_} = "
        lbl_input["text"] = f"{result}"
        showed_result = True

    # *********************** function clear_all **********************#
    def clear_all():
        global oper, result
        result = 0
        oper = ""
        lbl_input["text"] = ""
        lbl_history["text"] = ""

    def clear():
        input_ = lbl_input["text"]
        if input_:
            lbl_input["text"] = input_[:-1]

    # ******************************* percent handler ***************************#
    def percent():
        text = lbl_input["text"]
        if not text:
            return
        else:
            if "." in text or "e" in text:
                num = float(text)
            else:
                num = int(text)
            lbl_input["text"] = str(num / 100)

    # ******************************* remove zero handler ***************************#
    def remove_zero():
        global result
        res = str(result)
        if res[-2:] == ".0":
            result = res[:-2]
        else:
            result = res
        return result

    # **************************** btns ************************#
    num_pad = "789456123"
    opr_pad = "x-+"
    bottom_btns = ["+/-", "0", ".", "="]
    top_btns = ["CE", "C", "%", "/"]
    begin, end = 0, 3
    col = 0

    # ****************************top btns ************************#
    btn_clear_all = Button(frm_btn, text="CE", **btn_props, bg="burlywood", command=clear_all)
    btn_clear_all.grid(row=0, column=0)

    btn_clear = Button(frm_btn, text="C", **btn_props, bg="burlywood", command=clear)
    btn_clear.grid(row=0, column=1)
    btn_percent = Button(frm_btn, text="%", **btn_props, bg="burlywood", command=percent)
    btn_percent.grid(row=0, column=2)
    btn_div = Button(frm_btn, text="/", **btn_props, bg="burlywood", command=lambda x="/": opr_handler(x))
    btn_div.grid(row=0, column=3)

    # ***************************number btns ***********************#
    for row in range(1, 4):
        for j in range(begin, end):
            btn = Button(frm_btn, text=num_pad[j], **btn_props, command=lambda x=num_pad[j]: num_handler(x))
            btn.grid(column=col, row=row)
            col += 1
            # ********************* opr btns **********************#
        btn_opr = Button(frm_btn, text=opr_pad[row - 1], **btn_props, bg="burlywood",
                         command=lambda x=opr_pad[row - 1]: opr_handler(x))
        btn_opr.grid(column=3, row=row)
        begin, end = end, end + 3
        col = 0

    # *************************** bottom operator btns ********************#
    plus_minus = Button(frm_btn, text="+/-", **btn_props, bg="burlywood", command=change_sign)
    plus_minus.grid(row=4, column=0)
    btn_zero = Button(frm_btn, text="0", **btn_props, command=lambda: num_handler("0"))
    btn_zero.grid(row=4, column=1)
    btn_dot = Button(frm_btn, text=".", **btn_props, command=dot_handler)
    btn_dot.grid(row=4, column=2)
    btn_equals = Button(frm_btn, text="=", **btn_props, bg="burlywood", command=display_result)
    btn_equals.grid(row=4, column=3)

    window.mainloop()


calculator()
