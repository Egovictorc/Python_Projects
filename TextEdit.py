import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

def save_file():
    filepath = asksaveasfilename(
        defaultextension="*.txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as file:
        text = editor_text.get(1.0, tk.END)
        file.write(text)
        window.title(f"Advanced Text Editor - {filepath}")

def open_file():
    filepath = askopenfilename(filetypes=[
        ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as file:
        new_text = file.read()
        editor_text.delete(1.0, tk.END)
        editor_text.insert(tk.END, new_text)
        window.title(f"Advanced Text Editor - {filepath}")

window = tk.Tk()
window.title("Advanced Text Editor")
window.columnconfigure(1, weight=1, minsize=800)
window.rowconfigure(0, weight=1, minsize=800)

btn_frm = tk.Frame(master=window)

editor_text = tk.Text()
btn_open = tk.Button(master=btn_frm, text="Open", command=open_file)
btn_save = tk.Button(master=btn_frm, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", pady="10")
btn_save.grid(row=1, column=0, sticky="ew")

editor_text.grid(row=0, column=1, sticky="nsew")
btn_frm.grid(row=0, column=0, sticky="n")
window.mainloop()

