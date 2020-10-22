import os

def main():
    files = os.listdir(r"C:\Users\Dell\Desktop\projects")
    print(files)

main()



# import tkinter as tk
#
# """
# ou’ll build a temperature converter application
# that allows the user to input temperature in degrees Fahrenheit
# and push a button to convert that temperature to degrees Celsius.
# """
#
# window = tk.Tk()
# window.columnconfigure([0,1,2], weight=1)
# window.rowconfigure([0,1], weight=1, minsize=50)
# window.title("Temperature Converter")
# window.resizable(width=False, height=True)
#
# def handle_click():
#     temp_f = int(ent_temperature.get())
#     temp_c = (5/9)* (temp_f - 32)
#     lbl_result["text"] = f"={temp_c}"
#
#
# ent_temperature = tk.Entry()
# lbl_result = tk.Label(text="=", width=10)
# label_far = tk.Label(text="\N{DEGREE FAHRENHEIT}")
# label_cel = tk.Label(text="°C")
# lbl_info = tk.Label(text="Enter Temperature in degree")
# btn_convert = tk.Button(text="convert", command=handle_click)
#
#
# lbl_info.grid(row=0, column = 0)
# ent_temperature.grid(row=1, column = 0, sticky="we")
# label_far.grid(row=1, column = 1, sticky="w")
# lbl_result.grid(row=1, column = 2, sticky="e")
# label_cel.grid(row=1, column = 3, sticky="w")
# btn_convert.grid(row=1, column = 4)
#
# window.mainloop()