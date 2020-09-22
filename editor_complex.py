import tkinter as tk
from tkinter import filedialog as fd

class Editor():
    def __init__(self, master):
        self.master = master
        self.menubar = tk.Menu(self.master)

        self.file = tk.Menu(self.menubar, tearoff=0)
        self.file.add_command(label="Open")
        self.file.add_command(label="Open recent")
        self.file.add_command(label="Save as...")
        self.file.add_command(label="Exit", command=self.master.quit)

        self.edit = tk.Menu(self.menubar, tearoff=0)
        self.edit.add_command(label="Cut")
        self.edit.add_command(label="Copy")
        self.edit.add_command(label="Paste")
        self.edit.add_command(label="Delete")
        self.edit.add_command(label="Find")

        self.help = tk.Menu(self.menubar, tearoff=0)
        self.help.add_command(label="Help")
        self.help.add_command(label="Updates")
        self.help.add_command(label="About")

        self.menubar.add_cascade(menu=self.file, label="File")
        self.menubar.add_cascade(menu=self.edit, label="Edit")
        self.menubar.add_cascade(menu=self.help, label="Help")
        self.menubar.add_cascade(menu=self.help, label="Help")
        self.master.config(menu=self.menubar)

window = tk.Tk()
editor = Editor(window)
window.mainloop()