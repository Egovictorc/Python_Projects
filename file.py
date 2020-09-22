import tkinter as tk

window = tk.Tk()
menubar = tk.Menu(window)

file = tk.Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

test = tk.Menu(file, tearoff=0)

test.add_command(label="test 1")
test.add_command(label="test 2")
file.add_cascade(label="Test", menu=test)

file.add_separator()
file.add_command(label="Exit", command=window.quit)

edit = tk.Menu(menubar, tearoff=0)

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select all")

help = tk.Menu(menubar, tearoff=0)
help.add_command(label="About")
help.add_command(label="Updates")

menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="help", menu=help)

window.configure(menu=menubar)
window.mainloop()