from tkinter import *
from tkinter import messagebox

# from school_record.frames import signup
# from school_record.login import Signin
# import school_record.login as Signin

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

width = 800
height = 600

ypos = (screen_height - height) / 2
xpos = (screen_width - width) / 2


props = {

}

frm_props = {
    "bg": "burlywood"
}

lbl_props = {
    "bg": "burlywood",
    "font": ("arial", 14, "normal"),
    **props
}
btn_props = {
    "font": ("verdana", 13, "normal"),

    **props,
}
ent_props = {
    "width": 25,
    "bd": 2,
    "relief": SUNKEN,
    "font": ("arial", 14, "normal"),
    **props
}
frm_signup = ""


class Signup():
    def __init__(self, master):
        self.master = master
        self.master.title("NIIT Students Dashboard")
        self.master.resizable(width=False, height=False)
        self.master.geometry(f"{width}x{height}+{int(xpos)}+{int(ypos)}")
        self.master.config(bg="burlywood")

        self.main_frame = Frame(master, **frm_props)
        self.main_frame = Frame(master, **frm_props)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # self.main_frame = signup
        self.email = StringVar()
        self.password = StringVar()
        self.conf_password = StringVar()

        lbl_info = Label(self.main_frame, bg="burlywood", text="NIIT Students' Dashboard", font=("arial", 25, "normal"),
                         pady=20)
        lbl_info.pack()

        lbl_fields = [
            {"text": "Email Address"},
            {"text": "Password"},
            {"text": "Confirm Password"},
        ]
        ent_fields = [
            {"textvariable": self.email},
            {"textvariable": self.password, "show": "*"},
            {"textvariable": self.conf_password, "show": "*"},
        ]
        row = 0
        for j in range(0, len(lbl_fields)):
            lbl = Label(self.main_frame, **lbl_fields[j], **lbl_props)
            lbl.pack(fill=BOTH)

            row += 1
            ent = Entry(self.main_frame, **ent_fields[j], **ent_props)
            ent.pack(ipady=8, ipadx=8, pady=5)
            row += 1

        # *********************** btns ****************************#
        frm_login = Frame(self.main_frame, **frm_props)
        frm_login.pack()

        self.btn_register = Button(frm_login, pady=4, fg="#fff", text="REGISTER NOW", bg="dodger blue", **btn_props,
                                   command=self.register)
        self.btn_register.pack(fill="x", pady=5)

        self.lbl_login = Label(frm_login, text="Already have an account?", **lbl_props)
        self.lbl_login.pack(side=LEFT)
        self.btn_signin = Button(frm_login, bg="burlywood", text="Sign in", fg="red", bd="0", **btn_props, command=self.handle_signin)
        self.btn_signin.pack(side=LEFT)

    def register(self):
        email = self.email.get()
        password = self.password.get()
        conf_password = self.conf_password.get()

        if not (email or password or conf_password):
            messagebox.showerror(master=self.master, title="Incomplete details", message="All fields are required")
        elif not password == conf_password:
            messagebox.showwarning(master=self.master, title="Password not match", message="Password does not match")
        else:
            self.handle_signin()
            # signin = Signin(self.master)

    def handle_signin(self):
        from school_record.login import Signin
        from school_record.frames import frames
        signin = Signin(window)
        signin.frame.tkraise()
        frames.append({"name": "signup",
                       "frame": self.main_frame})

        # signin = Signin(self.master)
        self.main_frame.place_forget()


# signup.master.mainloop()
signup = Signup(window)

if __name__ == "__main__":
    window.mainloop()
    # window.mainloop()
