import tkinter as tk

window = tk.Tk()
window.geometry("450x300")
window.title("tk")

lbl_name = tk.Label(text=f"{'name'.title()}")
lbl_email = tk.Label(text=f"{'email'.title()}")
lbl_pwd = tk.Label(text=f"{'password'.title()}")

ent_name = tk.Entry()
ent_email = tk.Entry()
ent_pwd = tk.Entry()

ent_name.place(x=80, y=50)
ent_email.place(x=80, y=90)
ent_pwd.place(x=80, y=130)

lbl_name.place(x=30, y=50)
lbl_email.place(x=30, y=90)
lbl_pwd.place(x=30, y=130)

window.mainloop()