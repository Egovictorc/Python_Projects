from tkinter import *

bgc="burlywood"

root = Tk()
root.title("Scientific Calculator")
root.configure(background=bgc)
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("480x668+0+0")
root.resizable(height=False, width=False)
#root.geometry("%dx%d"%(sw, sh))
# print("coonfig: ", root.config())
# print("coonfigure: ", root.configure())
# print("coonfigure: ", root.geometry())
#help(Tk)


class Calculator:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.dsp_frame = Frame(master)
        #=======================Menu=======================================
        self.menubar = Menu(master)
        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label= "Standard")
        self.file.add_command(label="Scientific")
        self.file.add_separator()
        self.file.add_command(label="Exit")

        self.edit = Menu(self.menubar, tearoff=0)
        self.edit.add_command(label="Cut")
        self.edit.add_command(label="Copy")

        self.help = Menu(self.menubar, tearoff=0)
        self.help.add_command(label="About")
        self.help.add_command(label="Updates")

        self.menubar.add_cascade(label="File", menu=self.file)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.menubar.add_cascade(label="Help", menu=self.help)

        self.numpad = "789456123"
        self.hstDisplay = Label(self.dsp_frame, font=("aria", 20, "bold"), bg=bgc, justify=RIGHT, text="0", bd=30, relief=SUNKEN)
        self.txtDisplay = Label(self.dsp_frame, font=("aria", 20, "bold"), bg=bgc, justify=RIGHT, text="0", bd=30, relief=SUNKEN)
        #self.txtDisplay = Entry(self.frame, font=("aria", 20, "bold"), bg="powder blue", justify=RIGHT, text="0", bd=30, relief=SUNKEN)
        #self.txtDisplay.insert(0, "0")

        self.hstDisplay.pack(fill=X)
        self.txtDisplay.pack(fill=X)
        #self.txtDisplay.grid(column=0, row=0, columnspan=4, sticky=W+E)
        #self.txtDisplay.grid(column=0, row=0, columnspan=4, sticky=W+E)

        self.build_standard()
        #================== configure master =====================
        master.configure(menu=self.menubar)
        #self.frame.pack(fill="both")
        self.dsp_frame.pack(fill=X)
        self.frame.pack(fill=X)

        self.current = "0"
        self.total = 0
        self.operator = ""
        self.history = ""
        self.displayedResult = False

    def build_standard(self):
        count = 0
        for row in range(2,5):
            for col in range(3):
                btn_num = Button(self.frame, font=("arial", 20, "bold"), text=self.numpad[count], width=6, height=2, bd=4, command= lambda num = self.numpad[count]: self.disp_num(num))
                btn_num.grid(row=row, column=col, padx=2)
                count+=1
        #=============================OPERATORS ===========================
        btn_zero= Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="0", width=6, height=2, bd=4).grid(row=5, column=0, padx=1, pady=1)
        btn_dot= Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text=".", width=6, height=2, bd=4).grid(row=5, column=1, padx=1, pady=1)
        btn_pm= Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="+/-", width=6, height=2, bd=4).grid(row=5, column=2, padx=1, pady=1)
        btn_equals= Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="=", width=6, height=2, bd=4, command=self.result).grid(row=5, column=3, padx=1, pady=1)

        btn_clear = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="C", width=6, height=2,
                            bd=4).grid(row=1, column=0, padx=1, pady=1)
        btn_clear_all = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="CE", width=6, height=2,
                            bd=4, command=self.reset).grid(row=1, column=1, padx=1, pady=1)
        btn_sqrt = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="r", width=6, height=2,
                            bd=4).grid(row=1, column=2, padx=1, pady=1)
        btn_plus = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="+", width=6, height=2,
                            bd=4, command=lambda op= "+": self.operation(op)).grid(row=1, column=3, padx=1, pady=1)

        btn_minus = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="-", width=6, height=2,
                            bd=4, command=lambda op= "-": self.operation(op)).grid(row=2, column=3, padx=1, pady=1)
        btn_mult = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="x", width=6, height=2,
                            bd=4, command=lambda op= "x": self.operation(op)).grid(row=3, column=3, padx=1, pady=1)
        btn_div = Button(self.frame, font=("arial", 20, "bold"), bg=bgc, text="/", width=6, height=2,
                            bd=4, command=lambda op= "/": self.operation(op)).grid(row=4, column=3, padx=1, pady=1)



    def disp_num(self, new_num):
        #self.current = self.txtDisplay["text"]
        self.set_current()
        if self.current != "0":
            self.txtDisplay["text"] = self.current + new_num
            self.current = self.current + new_num
        else:
            self.txtDisplay["text"] = new_num
            self.current = new_num
        print(f"current: {self.current}\nnum:{new_num}")

    def operation(self, op):

        if self.operator:
            self.compute()
            print("%d: ", self.total)
        elif self.displayedResult:
            self.set_current()
            self.history = ""
            self.total = float(self.current)
            self.displayedResult = False
        else:
            self.total = float(self.current)
        self.operator = op
        self.add_history()
        self.txtDisplay["text"] = ""
        print(f"total: {self.total}\nop: {op}\nhist: {self.history}")

    def reset(self):
        self.total = 0
        self.current = "0"
        self.txtDisplay["text"] = "0"
        self.operator = ""
        self.hstDisplay["text"] = ""
        self.history = ""
        self.displayedResult = False

    def get_current(self):
        return self.current

    def set_current(self):
        self.current = self.txtDisplay["text"]

    def add_history(self):
        self.set_current()
        if not self.current:
            return
        if self.displayedResult or not self.history:
            self.history = f"{self.current} {self.operator}"
        else:
            self.history = f"{self.history} {self.current} {self.operator}"
        self.hstDisplay["text"] = f"{self.history}"

    def compute(self):
        self.set_current()
        if not self.current:
            return
        else:
            if self.operator == "+":
                self.total += float(self.current)
            elif self.operator == "-":
                self.total -= float(self.current)
            elif self.operator == "x":
                self.total *= float(self.current)
            elif self.operator == "/":
                self.total /= float(self.current)
            elif self.operator == "%":
                self.total %= float(self.current)


    def rem_zero(self, result):
        #remove zero decimal from result
        # implement later
        return str(result)

    def result(self):
        self.compute()
        self.operator = ""
        self.add_history()
        self.txtDisplay["text"] = self.rem_zero(self.total)
        self.displayedResult = True
        print("total: ", self.total)


casio = Calculator(root)
root.mainloop()