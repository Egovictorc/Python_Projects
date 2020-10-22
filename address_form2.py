from tkinter import *
from tkinter import messagebox

#=======================validate functions======================
def val_ent(val):
    if val.isalpha():
        return True
    else:
        return False

def ival_ent(val):
    print(f"{val} must be of string type")


#===================================submit function===================
def ask_submit(labels, entries):
    if messagebox.askokcancel(title="confim submit", message="can't edit after submission"):
        return submit(labels, entries)

def submit(labels, entries):
    for count, entry in enumerate(entries):
        if not entry.get():
            globals()["entry"] = None
        else:
            globals()["entry"] = entry.get()
        print(f"{labels[count]}=> {globals()['entry']}")

#===============================clear function=====================
def clear(entries):
    for entry in entries:
        if entry.get():
            entry.delete(0, END)

def ask_clear(entries):
    if messagebox.askyesno(title="Clear selection", message="Do you wish to clear selection?"):
        clear(entries)


root = Tk()
root.title("Registration Form")
root.resizable(height=False, width=False)


#=========================Label Frame ========================================================
frame_lbl = Frame(root, bg="powder blue")
frame_btn = Frame(root)
frame_lbl.pack(fill=X)
frame_lbl.columnconfigure(1, weight=1)
frame_btn.pack(fill=X)

vcmd = frame_lbl.register(val_ent)
ivcmd = frame_lbl.register(ival_ent)
field_list = [
    "First Name","Last Name","Age", "City", "State", "Country"
]
entry_list = []

for count, field in enumerate(field_list):
    label = Label(frame_lbl, text=f"{field}:", font=("arial", 11, "normal"), bg="powder blue")
    label.grid(column =0, row=count, sticky=E, pady=4, padx=5)

    entry = Entry(frame_lbl, width=70, validate="key", invalidcommand=(ivcmd, "%P"),validatecommand=(vcmd, "%P"))
    entry.grid(column=1, row=count, sticky=E+W+N+S, pady=2)
    entry_list.append(entry)


btn_submit = Button(frame_btn, text="Submit", bg="#99a2ff", command= lambda x= field_list, y = entry_list: ask_submit(x, y))
btn_submit.pack(side=RIGHT, ipadx=5, ipady=5, padx=5, pady=5)
btn_clear = Button(frame_btn, text="clear", bg="#ff99bb", command=lambda x=entry_list: ask_clear(entry_list))
btn_clear.pack(side=RIGHT, ipadx=5, ipady=5, pady=5)

root.mainloop()