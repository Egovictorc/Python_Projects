from tkinter import Tk, Button, Label, Entry

parent = Tk()

email = Label(parent, text="Email:")
email.grid(row=0, column=0)

email_entry = Entry(parent)
email_entry.grid(row=0, column=1)

password = Label(parent, text="Password")
password.grid(row=1, column=0)

password_entry = Entry(parent)
password_entry.grid(row=1, column=1)

submit_btn = Button(parent, text="Submit Now", bg="burlywood")
submit_btn.grid(row=2, column=0, sticky="nswe")

parent.mainloop()
