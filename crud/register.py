from tkinter import *

window = Tk()
window.title("Registration page")

def login():
    pass

def hav_acc():
    window.destroy()
    from login import open_login
    open_login()
    #window.title("Login page")

frame = Frame(window)
frame.pack()

lbl_info = Label(master=frame, text="User Registration form")
lbl_info.grid(column=0, row=0, columnspan=2, sticky="news")

####***************** labels **********************
fname = Label(master=frame, text="First Name: ")
lname = Label(master=frame, text="Last Name: ")
city = Label(master=frame, text="City: ")
email= Label(master=frame, text="Email: ")

fname.grid(column=0, row=1, sticky="w")
lname.grid(column=0, row=2, sticky="w")
city.grid(column=0, row=3, sticky="w")
email.grid(column=0, row=4, sticky="w")

#******************** entry *************
fname_entry = Entry(master=frame, width=65)
lname_entry = Entry(master=frame, width=65)
city_entry = Entry(master=frame, width=65)
email_entry = Entry(master=frame, width=65)

fname_entry.grid(column=1, row=1)
lname_entry.grid(column=1, row=2)
city_entry.grid(column=1, row=3)
email_entry.grid(column=1, row=4)

btn_submit = Button(frame, text="Submit", command=login)
btn_hav_acc = Button(frame, text="Already Have Account? login", command=hav_acc)
btn_submit.grid(column=1, row=5, sticky="e")
btn_hav_acc.grid(column=0, row=6, columnspan=2, sticky="news")


##********** login page ************##
login_frame = Frame(window)
login_frame.pack()

def signup():
    .destroy()
    start_reg()

label_welcome = Label(login_frame, text="Welcome to Login page")
btn_reg = Button(login_frame, text="Don't have account? Sign up", command=signup)
label_welcome.pack()
btn_reg.pack()

# def start_reg():
#     window.mainloop()
#
# if __name__ == "__main__":
#     start_reg()