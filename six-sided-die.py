import tkinter as tk
import random

"""Write a program that simulates rolling 
a six-sided die. 
There should be one button with the text "Roll". 
When the user clicks the button, a random integer from 1 to 6 should be displayed.
"""

window = tk.Tk()
window.title("six sided die")
window.columnconfigure(0, weight=1, minsize=25)
window.rowconfigure([0,1], weight=1, minsize=25)

def handle_click():
    num = random.randint(0, 6)
    label["text"] = f"{num}"


btn_roll = tk.Button(text="Roll", width=25, command=handle_click)
btn_roll.grid(row=0, column=0, sticky="nsew")

label = tk.Label(text="4", width=25)
label.grid(row=1, column=0, sticky="nsew")

window.mainloop()