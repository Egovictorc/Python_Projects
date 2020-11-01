from tkinter import *

window = Tk()

props = {
    "font": ("arial", 20, "bold")
}

lbl_props = {
    "relief": SUNKEN,
    "borderwidth": 15,
    "background": "burlywood",
    "padx": 10,
    "pady": 10,
    **props
}

btn_props = {
    "relief": SUNKEN,
    "borderwidth": 5,
    "background": "aliceblue",
    "height": 2,
    "width": 5,
    **props
}

frame_props = {

}

class Calc:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        #self.master.geometry("450x600")

        #************************* frames ****************************#
        self.frm_label = Frame(self.master)
        self.frm_btn = Frame(self.master)

        #*********************** screens **************************#
        self.lbl_history = Label(self.frm_label, **lbl_props)
        self.lbl_input = Label(self.frm_label, **lbl_props)

        self.lbl_history.pack(fill=BOTH)
        self.lbl_input.pack(fill=BOTH)
        self.create_btn()

        self.frm_label.pack(fill=BOTH)
        self.frm_btn.pack(fill=BOTH)

        self.operator = ""
        self.result = 0

    def create_btn(self):
        nums = "789456123"
        operators ="x-+="
        btn_bottom = ["+/-", 0, ".", "="]
        btn_top = ["C", "CE", "r", "/"]
        begin, row, col = 0, 0, 0
        end = 3

        #***********************************number btns ***********************#
        for i in range(1, 4):
            for j in range(begin, end):
                #**************** number btns*********************#
                text = nums[j]
                btn = Button(self.frm_btn, text=text, **btn_props, command= lambda x=text: self.num_handler(x))
                btn.grid(row=i, column=col)
                col += 1
            #*****************operator btns ****************************#
            btn = Button(self.frm_btn, text=operators[i-1 ], **btn_props,
                         command= lambda x = operators[i-1]: self.opr_handler(x), bg="burlywood")
            btn.grid(column=col, row=i)
            col = 0
            begin = end
            end += 3
        # *****************bottom operator btns ****************************#
        plus_minus = Button(self.frm_btn, text="+/-", **btn_props, bg="burlywood",
                          command= self.change_sign)
        plus_minus.grid(column=0, row=4)
        btn_zero = Button(self.frm_btn, text="0", **btn_props, bg="burlywood",
                          command=lambda x= "0": self.num_handler(x))
        btn_zero.grid(column=1, row=4)
        btn_dot = Button(self.frm_btn, text=".", **btn_props, bg="burlywood",
                          command=self.dot_handler)
        btn_dot.grid(column=2, row=4)
        btn_equals = Button(self.frm_btn, text="=", **btn_props, bg="burlywood",
                          command= self.display_result)
        btn_equals.grid(column=3, row=4)

        # *****************top operator btns ****************************#
        for i, j in enumerate(btn_top):
            if i == 0 or i == 1:
                continue
            btn = Button(self.frm_btn, text=j, **btn_props, bg="burlywood",
                         command= lambda x = j: self.opr_handler(x))
            btn.grid(column=i, row=0)
            btn_clear_all = Button(self.frm_btn, text="CE", **btn_props, bg="burlywood",
                         command= self.clear)
            btn_clear_all.grid(column=1, row=0)
            btn_clear = Button(self.frm_btn, text="C", **btn_props, bg="burlywood",
                         command= self.clear)
            btn_clear.grid(column=0, row=0)

    def num_handler(self, btn_text):
        text = self.lbl_input["text"]

        if not text:
            self.lbl_input["text"] = btn_text
        else:
            self.lbl_input["text"] = text + btn_text


    # *********************** function number handler **********************#
    def dot_handler(self):
        text = self.lbl_input["text"]
        if "." in text:
            return
        else:
            self.num_handler(".")

    def opr_handler(self, opr):
        cur_text = self.lbl_input["text"]
        cur_hist = self.lbl_history["text"]

        if not cur_text and self.operator:
            return
        elif not self.operator:
            self.result = float(cur_text)
            self.operator = opr
            self.lbl_history["text"] = f"{cur_text} {opr}"
            self.lbl_input["text"] = ""
        else:
            self.compute()
            self.operator = opr
            self.lbl_history["text"] = f"{cur_hist} {cur_text} {opr}"
            self.lbl_input["text"] = str(self.result)

    def compute(self):
        opr = self.operator
        num = float(self.lbl_input["text"])
        if opr == "+":
            self.result += num
        elif opr == "-":
            self.result -= num
        elif opr == "x":
            self.result *= num
        elif opr == "/":
            self.result /= num

    def clear(self):
        self.lbl_history["text"] = ""
        self.lbl_input["text"] = ""
        self.result = 0
        self.operator = ""
        print("cleared ", self.result)

    def display_result(self):
        self.compute()
        hist = self.lbl_history["text"]
        num =  self.lbl_input["text"]
        self.lbl_history["text"] = f"{hist} {num} ="

        self.lbl_input["text"] = self.rem_zero()

    def change_sign(self):
        num = float(self.lbl_input["text"])
        self.lbl_input["text"] = str(-1 * num)

    def rem_zero(self):
        after_dot = str(self.result)[-2:]
        if after_dot == ".0":
            return str(self.result)[:-2]
        else:
            return str(self.result)

calc = Calc(window)
calc.master.mainloop()