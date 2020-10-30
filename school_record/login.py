from tkinter import *
from tkinter import messagebox
import school_record.model as model
props = {
    "font": ("arial", 14, "normal"),
}

frm_props = {
"bg": "burlywood"
}

lbl_props = {
"bg": "burlywood",
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
    **props
}


class Signin():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.frame = Frame(master, width=300, height=400, bg="burlywood")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        lbl_info = Label(self.frame, bg="burlywood", text="Enter details to login", font=("arial", 25, "normal"),
                         pady=20)
        lbl_info.pack()

        self.email = StringVar()
        self.password = StringVar()

        lbl_fields = [
            {"text": "Email Address"},
            {"text": "Password"},
        ]
        ent_fields = [
            {"textvariable": self.email},
            {"textvariable": self.password},
        ]
        row = 0
        for j in range(0, len(lbl_fields)):
            lbl = Label(self.frame, **lbl_fields[j], **lbl_props)
            lbl.pack(fill=BOTH)

            row += 1
            ent = Entry(self.frame, **ent_fields[j], **ent_props)
            ent.pack(ipady=8, ipadx=8, pady=5)

        btn_signin = Button(self.frame, pady=4, fg="#fff", text="LOGIN", bg="dodger blue",
                                   **btn_props, command=self.handle_login)
        btn_signin.pack(fill="x", pady=15)


        # *********************** btns ****************************#
        frm_register = Frame(self.frame, **frm_props)
        frm_register.pack()

        self.lbl_register = Label(frm_register, text="Dont't have an account?", **lbl_props)
        self.lbl_register.pack(side=LEFT)
        self.btn_signup = Button(frm_register, text="Sign up", fg="red", bd="0", bg="burlywood", **btn_props,
                                 command=self.handle_signup)
        self.btn_signup.pack(side=LEFT)

        #self.frame.tkraise()


    def handle_login(self):
        email = self.email.get()
        password = self.password.get()

        if not (email and password):
            messagebox.showerror(master=self.master, title="Incomplete details", message="All fields are required")
        else:
            from . import model as model
            #import school_record.model as model
            model = model.Model()
            result = model.get_records()
            print(result)
            #signin = Signin(self.master)

    def handle_signup(self):
        from school_record.frames import frames

        for frm in frames:
            if frm["name"] == "signup":
                #print(frm["frame"])
                frm["frame"].place(relx=0.5, rely=0.5, anchor="center")
                frm["frame"].tkraise()
        self.frame.place_forget()

        #from school_record.signup import Signup
        #signup = Signup(self.master)
        #signup = signup.Signup(self.master)
        #signup.main_frame.tkraise()