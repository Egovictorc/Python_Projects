from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import asksaveasfilename, askopenfilename, askopenfile


def save_as_file():
    filepath = asksaveasfilename(
        defaultextension="*.txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as file:
        text = editor_text.get(1.0, END)
        file.write(text)
        window.title(f"Advanced Text Editor - {filepath}")

filename = ""
def save_file():
    global filename
    askSave= mb.askokcancel(title="Save file", message="Click ok to save")
    if askSave:
        if not filename:
            return
        with open(filename, "w") as file:
            text = editor_text.get(1.0, END)
            file.write(text)
            window.title(f"Advanced Text Editor - {filename}")
            mb.showinfo(title="Success Message", message="File saved successfully")

# def open_file():
#     filepath = askopenfilename(filetypes=[
#         ("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     print("filepath ", filepath)
#     if not filepath:
#         return
#     with open(filepath, "r") as file:
#         new_text = file.read()
#         editor_text.delete(0.0, END)
#         editor_text.insert(END, new_text)
#         window.title(f"Advanced Text Editor - {filepath}")
def open_file():
    global filename
    filepath = askopenfile(filetypes=[
        ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    filename = filepath.name
    print("filepath ", filepath)
    if not filepath:
        return
    new_text = filepath.read()
    editor_text.delete(0.0, END)
    editor_text.insert(END, new_text)
    window.title(f"Advanced Text Editor - {filepath.name}")

window = Tk()
window.title("Advanced Text Editor")
#window.geometry("800x800")
window.columnconfigure(1, minsize=800, weight=1)
window.rowconfigure(0, minsize=800)

btn_frm = Frame(master=window)
editor_text = Text()

btn_open = Button(master=btn_frm, text="Open", command=open_file)
btn_save = Button(master=btn_frm, text="Save", command=save_file)
btn_save_as = Button(master=btn_frm, text="Save As", command=save_as_file)

btn_open.grid(row=0, column=0, sticky="ew", pady="10")
btn_save.grid(row=1, column=0, sticky="ew")
btn_save_as.grid(row=2, column=0, sticky="ew")

editor_text.grid(row=0, column=1, sticky="nsew")
btn_frm.grid(row=0, column=0, sticky="n")
window.mainloop()

