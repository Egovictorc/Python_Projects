from tkinter import *

title_props = {
    "font": ("verdana", 16)
}

lbl_props = {
    "font": ("arial", 14),
}

btn_props = {
    "padx": 5
}

def main():
    window = Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    width = 800
    height = 600

    ypos = (screen_height - height ) / 2
    wpos = (screen_width - width ) / 2

    window.title("Registration form")
    window.geometry(f"{width}x{height}+{int(wpos)}+{int(ypos)}")

    #*********************** frames ********************************#
    frm_signup = Frame(window, )
    frm_signin = Frame(window, )

    frm_signup_cont = Frame(frm_signup)
    frm_signin_cont = Frame(frm_signin)

    for f in (frm_signup_cont, frm_signin_cont):
        f.place(relx=0.5, rely=0.3, anchor=CENTER)

    frames = {}
    for f in (frm_signup, frm_signin):
        frames[f] = f
        f.grid(row=0, column=0, sticky="news")


    #*************************** common widgets *************************#
    signin_title = Label(frm_signin_cont, text="Welcome from signin page", **title_props)
    signup_title = Label(frm_signup_cont, text="Welcome from signup page", **title_props)

    for lbl in (signin_title, signup_title):
        lbl.grid(row=0, column=0, columnspan=2, pady=30)

    #***********************function show frame *************************
    def show_frame(frm):
        frame = frames[frm]
        frame.tkraise()

    #*********************** signup widgets ********************#
    lbl_list = ["Email", "Password"]

    for i in range(0, len(lbl_list) ):
        label = Label(frm_signup_cont, text=lbl_list[i], **lbl_props)
        label.grid(row=i+1, column=0, sticky="w", pady=5)

        field = Entry(frm_signup_cont, width=40)
        field.grid(row=i+1, column=1, sticky="ewsn", pady=5)

    btn_signup = Button(frm_signup_cont, text="Sign up", **btn_props, command = lambda sc = frm_signin: show_frame(sc))
    btn_signup.grid(row=3, column=1, sticky=E)

    #*********************** signin widgets ********************#
    lbl_list = ["Email", "Password"]

    for i in range(0, len(lbl_list) ):
        label = Label(frm_signin_cont, text=lbl_list[i], **lbl_props)
        label.grid(row=i+1, column=0)

        field = Entry(frm_signin_cont)
        field.grid(row=i+1, column=1, sticky="ewsn")

    btn_signup = Button(frm_signin_cont, text="Sign up", **btn_props, command = lambda sc = frm_signup: show_frame(sc))
    btn_signup.grid(row=3, column=1, sticky=E)

    window.mainloop()

main()