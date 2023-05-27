from tkinter import *

window = Tk()
window.geometry("450x500")
window.resizable(width=False, height=False)

frame1 = Frame(window, bg="red")
frame2 = Frame(window, bg="#23ffaa")
frame3 = Frame(window, bg="burlywood")
frame4 = Frame(window, bg="#fe1a99")

#frame1.pack(fill=BOTH, expand=True)
#frame2.pack(fill=BOTH, expand=True)
#frame3.pack(fill=BOTH, expand=True)
#frame4.pack(fill=BOTH, expand=True)

frames = {
    0: frame1,
    1: frame2,
    2: frame3,
    3: frame4
}

# commands
print(frames)
for index, frm in enumerate(frames):
    print(frm)

def prev_page(cur_index ):
    frames[cur_index].pack_forget()
    if cur_index <= 0:
        index  = 3
        frames[index].pack(fill=BOTH, expand=True)
    else:
        frames[cur_index - 1].pack(fill=BOTH, expand=True)


def next_page(cur_index):
    frames[cur_index].pack_forget()
    if cur_index >= 3:
        index  = 0
        frames[index].pack(fill=BOTH, expand=True)
    else:
        frames[cur_index + 1].pack(fill=BOTH, expand=True)

for index, frm in enumerate(frames):
    label = Label(frames[frm], text =f"Welcome to page {frm + 1} ")
    label.pack()

    btn_prev = Button(frames[frm], text = f"Visit page {frm}", command= lambda x=frm : prev_page(x))
    btn_next = Button(frames[frm], text = f"Visit page {frm + 2}", command= lambda x=frm : next_page(x))

    label.pack()
    btn_prev.pack(side=LEFT)
    btn_next.pack(side=RIGHT)




window.mainloop()