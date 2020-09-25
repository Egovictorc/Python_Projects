import tkinter as tk

window = tk.Tk()

fields = [
    "First Name", "Last Name", "Address Line 1", "Address Line 2",
    "City", "State/Province", "Postal Code", "Country"
]
frame = tk.Frame(borderwidth=3, relief=tk.SUNKEN)
frame.pack()

for r, field in enumerate(fields):
    label = tk.Label(master=frame, text=f"{field}:")
    label.grid(row=r, column=0, sticky="e", padx=5, pady=5)

    entry = tk.Entry(master=frame, width=70)
    entry.grid(row=r, column=1, sticky="ns", pady=2)

btn_frame = tk.Frame(master=window)
btn_frame.pack(fill=tk.X)

submit = tk.Button(master=btn_frame, text="Submit", fg="green")
submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

clear = tk.Button(master=btn_frame, text="Clear", fg="red")

def handle_key(e):
    print(e.char())
    print("clear pressed")


window.bind("key", handle_key)
clear.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.title("Registration Form")
window.mainloop()