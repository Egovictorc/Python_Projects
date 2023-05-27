from tkinter import *

count = 0
parent = Tk()

def handle_click():
    global count
    count = count + 1
    print(f"button clicked {count}")
btn= Button(parent, text= "Click me", bg="black", fg="#fff",
            command=handle_click, borderwidth=10, relief=SUNKEN,
            activebackground="red"
            )
btn.pack()


parent.mainloop()