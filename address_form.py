import tkinter as tk
from tkinter import messagebox


window = tk.Tk()

lbl_dict = {}
ent_dict = {}
ent_ls =[]

def validate(val):
    if val.isalpha():
        return True
    return False

def ivalidate(val):
    messagebox.showwarning( title="no op", message=f"{val}: incorrect type")
    print(f"{val}: incorrect type")

def reset(entries):
    #print(ent_dict)
    if not messagebox.askokcancel(title="clear values", message="click ok to clear values"):
        return
    for key in entries:
        key.delete("0", tk.END)

def askSubmit(data):
    if not messagebox.askokcancel(title="confirm", message="NB: You can't edit after submission\nclick ok to submit"):
        return
    showData(*data)

def showData(lbl_dict, ent_ls):
    for i, k in enumerate(lbl_dict.keys()):
        #print(f" {k} -> {ent_dict[k].get()}")
        print(f" {k} -> {ent_ls[i].get()}")
    for key in ent_ls:
        key.delete("0", tk.END)

def map_val(lbl, ent):
    lbl_dict[lbl] = ent.get()


fields = [
    "First Name", "Last Name", "Address Line 1", "Address Line 2",
    "City", "State/Province", "Postal Code", "Country"
]
frame = tk.Frame(borderwidth=3, relief=tk.SUNKEN)
frame.pack()

vcmd = frame.register(validate)
ivcmd = frame.register(ivalidate)

for r, field in enumerate(fields):
    label = tk.Label(master=frame, text=f"{field}:")
    label.grid(row=r, column=0, sticky="e", padx=5, pady=5)

    entry = tk.Entry(master=frame, width=70, validate="key", invalidcommand=(ivcmd, "%P"), validatecommand=(vcmd, "%P") )
    ent_dict[f"{field}"] = tk.StringVar()
    entry["textvariable"] = ent_dict[f"{field}"]
    ent_ls.append(entry)
    entry.grid(row=r, column=1, sticky="ns", pady=2)

    lbl_dict[field] = ""

btn_frame = tk.Frame(master=window)
btn_frame.pack(fill=tk.X)

submit = tk.Button(master=btn_frame, text="Submit", fg="green")
submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
#submit["command"] = lambda x = (lbl_dict, ent_dict): showData(*x)
submit["command"] = lambda x = (lbl_dict, ent_ls): askSubmit(x)

clear = tk.Button(master=btn_frame, text="Clear", fg="red")
clear["command"] = lambda x = ent_ls: reset(x)

def handle_key(e):
    print(e.char())
    print("clear pressed")


window.bind("key", handle_key)
clear.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.title("Registration Form")
window.mainloop()