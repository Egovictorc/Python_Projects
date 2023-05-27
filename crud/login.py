from tkinter import *

window_login = Tk()
window_login.title("Login page")
login_frame = Frame(window_login)
login_frame.pack()

def signup():
    window_login.destroy()
    from register import start_reg
    start_reg()


label_welcome = Label(login_frame, text="Welcome to Login page")
btn_reg = Button(login_frame, text="Don't have account? Sign up", command=signup)
label_welcome.pack()
btn_reg.pack()


def open_login():
    window_login.mainloop()


if __name__ == "__main__":
    open_login()
