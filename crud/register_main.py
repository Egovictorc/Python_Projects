from tkinter import *

window = Tk()
window.title("Registration page")
window.geometry("500x400")
def login():
    pass
def hav_acc():
    window.title("Login page")
    register_frame.pack_forget()
    login_frame.pack()
    #window.title("Login page")

##****************** Registration page ***************
register_frame = Frame(window)
register_frame.pack()

lbl_info = Label(master=register_frame, text="User Registration form")
lbl_info.grid(column=0, row=0, columnspan=2, sticky="news")

####***************** labels **********************
fname = Label(master=register_frame, text="First Name: ")
lname = Label(master=register_frame, text="Last Name: ")
city = Label(master=register_frame, text="City: ")
email= Label(master=register_frame, text="Email: ")

fname.grid(column=0, row=1, sticky="w")
lname.grid(column=0, row=2, sticky="w")
city.grid(column=0, row=3, sticky="w")
email.grid(column=0, row=4, sticky="w")

#******************** entry *************
fname_entry = Entry(master=register_frame, width=65)
lname_entry = Entry(master=register_frame, width=65)
city_entry = Entry(master=register_frame, width=65)
email_entry = Entry(master=register_frame, width=65)

fname_entry.grid(column=1, row=1)
lname_entry.grid(column=1, row=2)
city_entry.grid(column=1, row=3)
email_entry.grid(column=1, row=4)

btn_submit = Button(register_frame, text="Submit", command=login)
btn_hav_acc = Button(register_frame, text="Already Have Account? login", command=hav_acc)
btn_submit.grid(column=1, row=5, sticky="e")
btn_hav_acc.grid(column=0, row=6, columnspan=2, sticky="news")


##********** login page ************##
login_frame = Frame(window)
#login_frame.pack()

def signup():
    window.title("Registration page")
    login_frame.pack_forget()
    register_frame.pack()

label_welcome = Label(login_frame, text="Welcome to Login page")
field_frame = Frame(login_frame)
field_frame.pack()
####***************** labels **********************
email= Label(master=field_frame, text="Email: ")
password= Label(master=field_frame, text="Password: ")

email.grid(column=0, row=0, sticky="w")
password.grid(column=0, row=1, sticky="w")

#******************** entry *************
password_entry = Entry(master=field_frame, width=65)
email_entry = Entry(master=field_frame, width=65)

email_entry.grid(column=1, row=0, sticky="w")
password_entry.grid(column=1, row=1, sticky="w")
btn_reg = Button(login_frame, text="Don't have account? Sign up", command=signup)
label_welcome.pack()
btn_reg.pack()

window.mainloop()
