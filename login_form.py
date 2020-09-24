import tkinter as tk

window = tk.Tk()

lblname = tk.Label(window, text="Name")
lblname.place(anchor="nw")
lblpwd = tk.Label(window, text="Password")
lblpwd.place(x=30, y = 90)

btnsubmit = tk.Button(window, text="Submit")
btnsubmit.place(x=100,y =130)

entname = tk.Entry(window, selectbackground="red", selectforeground="blue")
entname.place(x=100, y = 50)
entpwd = tk.Entry(window)
entpwd.place(x=100, y=90)


# using grid geometry manager
# lblname = tk.Label(window, text="Name")
# lblname.grid(row=0, column=0)
# lblpwd = tk.Label(window, text="Password")
# lblpwd.grid(row=1, column=0)
#
# btnsubmit = tk.Button(window, text="Submit")
# btnsubmit.grid(row=2, column=0)
#
# entname = tk.Entry(window)
# entname.grid(column=1, row=0)
# entpwd = tk.Entry(window)
# entpwd.grid(column=1, row=1 )


window.mainloop()



#using place geometry method
# window = tk.Tk()
# window.geometry("450x300")
# window.title("tk")
#
# lbl_name = tk.Label(text=f"{'name'.title()}")
# lbl_email = tk.Label(text=f"{'email'.title()}")
# lbl_pwd = tk.Label(text=f"{'password'.title()}")
#
# ent_name = tk.Entry()
# ent_email = tk.Entry()
# ent_pwd = tk.Entry()
#
# ent_name.place(x=80, y=50)
# ent_email.place(x=80, y=90)
# ent_pwd.place(x=80, y=130)
#
# lbl_name.place(x=30, y=50)
# lbl_email.place(x=30, y=90)
# lbl_pwd.place(x=30, y=130)
#
# window.mainloop()