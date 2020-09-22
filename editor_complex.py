import tkinter as tk
from tkinter import filedialog as fd

class Editor():
    def __init__(self, master):
        self.master = master
        self.master.title("NIIT Editor")
        self.text_editor = tk.Text(self.master, fg="#fefefe", bg="#555")
        self.text_editor.insert(1.0, "Edit your text here")
        self.text_editor.pack(fill=tk.BOTH, expand=1)
        self.createMenu()

        self.open_filepath = ""

    def createMenu(self):
        """create editor top menubar"""
        menubar = tk.Menu(self.master)
        file = tk.Menu(menubar, tearoff=0)
        edit = tk.Menu(menubar, tearoff=0)
        help_ = tk.Menu(menubar, tearoff=0)

        #file menus
        file.add_command(label="Open", command=self.open)
        file.add_command(label="Save", command=self.save)
        file.add_command(label="Open recent")
        file.add_command(label="Save as...", command=self.save_as)
        file.add_command(label="Exit", command=self.master.quit)

        #edit menus
        edit.add_command(label="Cut")
        edit.add_command(label="Copy")
        edit.add_command(label="Paste")
        edit.add_command(label="Delete")
        edit.add_command(label="Find")

        help_.add_command(label="Help")
        help_.add_command(label="Updates")
        help_.add_command(label="About")

        menubar.add_cascade(menu=file, label="File")
        menubar.add_cascade(menu=edit, label="Edit")
        menubar.add_cascade(menu=help_, label="Help")

        self.master.config(menu=menubar)

    def open(self):
        """open file for editing"""
        filepath = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        self.open_filepath  = filepath
        if not filepath:
            return
        with open(filepath, "r") as file:
            text = file.read()
            self.master.title(f"NIIT Editor:- {filepath}")
            self.text_editor.insert(tk.INSERT, text)
            print(text)

    def save(self):
        """save file"""
        with open(self.open_filepath, "w") as file:
            text = self.text_editor.get("1.0", tk.END)
            file.write(text)

    def save_as(self):
        """save file"""
        filepath = fd.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "w") as file:
            text = self.text_editor.get(1.0, tk.END)
            file.write(text)

window = tk.Tk()
editor = Editor(window)
window.mainloop()