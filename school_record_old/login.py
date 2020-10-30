from tkinter import *
from tkinter import messagebox

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
    **props,
"bg": "burlywood"
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
            ent.pack()

        btn_signin = Button(self.frame, pady=4, fg="#fff", text="LOGIN", bg="dodger blue",
                                   command=self.handle_login)
        btn_signin.pack(fill="x", pady=15)
        btn_signup = Button(self.frame, pady=4, fg="#fff", text="Go back", bg="dodger blue",
                                   command=self.handle_signup)
        btn_signup.pack(fill="x", pady=15)

        #self.frame.tkraise()


    def handle_login(self):
        email = self.email.get()
        password = self.password.get()

        if not (email or password):
            messagebox.showerror(master=self.master, title="Incomplete details", message="All fields are required")
        else:
            pass
            signin = Signin(self.master)

    def handle_signup(self):
        from school_record.frames import frames
        for frm in frames:
            if frm["name"] == "signup":
                print(frm["frame"])
                frm["frame"].place(relx=0.5, rely=0.5, anchor="center")
                frm["frame"].tkraise()
        #from school_record.signup import Signup
        #signup = Signup(self.master)
        self.frame.place_forget()
        #signup = signup.Signup(self.master)
        #signup.main_frame.tkraise()