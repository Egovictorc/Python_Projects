import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd


class Editor():
    def __init__(self, master):
        self.master = master
        master.title("NIIT Editor")
        self.text_editor = tk.Text(master, fg="#fefefe", bg="#555")
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

        # file menus
        file_menu = [
            {"label": "Open",
             "command": self.open
             }, {
                "label": "Save",
                "command": self.save
            }, {
                "label": "Open recent",
            }, {
                "label": "Save as...",
                "command": self.save_as
            }, {
                "label": "Exit",
                "command": self.exit
            },
        ]
        for menu in file_menu:
            file.add_command(**menu)

        # edit menus
        edit_menu = [
            {"label": "Copy"},
            {"label": "Cut"},
            {"label": "Paste"},
            {"label": "Delete"},
            {"label": "Find"},
        ]
        for menu in edit_menu:
            edit.add_command(**menu)

        #help menus
        help_menu = [
            {"label": "Help"},
            {"label": "Update"},
            {"label": "About"},
        ]
        for menu in help_menu:
            help_.add_command(**menu)

        menubar.add_cascade(menu=file, label="File")
        menubar.add_cascade(menu=edit, label="Edit")
        menubar.add_cascade(menu=help_, label="Help")

        self.master.config(menu=menubar)

    def open(self):
        """open file for editing"""
        filepath = fd.askopenfilename(title="Select file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                                      )
        self.open_filepath = filepath
        if not filepath:
            return
        with open(filepath, "r") as file:
            text = file.read()
            self.master.title(f"NIIT Editor:- {filepath}")
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert("1.0", text)

    def save(self):
        """save file"""
        with open(self.open_filepath, "w") as file:
            text = self.text_editor.get("1.0", tk.END)
            file.write(text)

    def save_as(self):
        """save as file"""
        filepath = fd.asksaveasfilename(defaultextension="txt", filetypes=[("Text Documents(*.txt)", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "w") as file:
            text = self.text_editor.get(1.0, tk.END)
            file.write(text)

    def exit(self):
        if messagebox.askyesno(title="confirm exit", message="Do you wish to exit?"):
            self.master.quit()
        else:
            print("no exit")



window = tk.Tk()
window.geometry("450x400-0-1")
editor = Editor(window)
window.mainloop()
