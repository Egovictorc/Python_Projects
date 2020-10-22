import requests
import bs4
from time import sleep
import json



pages = ['https://www.allsides.com/media-bias/media-bias-ratings',
    'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
    'https://www.allsides.com/media-bias/media-bias-ratings?page=2']
data = []

def make_request():
    for page in pages:
        response = requests.get('https://www.allsides.com/media-bias/media-bias-ratings')
        response.raise_for_status()
        content = response.content
        soup = bs4.BeautifulSoup(content, "html.parser")
        rows = soup.select("tbody tr")

        for row in rows:
            d = dict()
            d["name"] = row.select_one(".source-title").text.strip()
            d["allsides_page"] = "https://www.allsides.com" +row.select_one(".source-title a")["href"]
            d["bias"] = row.select_one(".views-field-field-bias-image a")['href'].split("/")[-1]
            d["agree"] = int(row.select_one(".agree").text)
            d["disagree"] = int(row.select_one(".disagree").text)
            d["agree_ratio"] = d["agree"] / d["disagree"]
            d["agreeance_text"] = d["agree_ratio"]

            data.append(d)

        print(data[0])
        sleep(10)

make_request()

d =  {
    "name": "uche",
    "age": 7,
    "city": "onitsha"
}
with open("allsides.json", "w") as f:
    json.dump(data, f, indent=4)

# bias = row.select_one('.views-field-field-bias-image a')['href'].split("/")[-1
# all_bias = bias.split("/")
# last_bias = all_bias[-1]
# print(all_bias)
# print(last_bias)
#
#
# y = [x for x in (1,2,3,4,5)]
# print(5) if 5 in [3,4,5,6,7] else 4
# print(y)


# import os
#
# def main():
#     with open("text.txt") as f:
#         content = f.read()
#         verify = content.splitlines()
#         print(content)
#         print("verify ", verify)
#
#     files = os.listdir()
#     print(files)
#
# main()
#
#
# # import tkinter as tk
# # root = tk.Tk()
# # help(tk.StringVar())
# #
# # window = tk.Tk()
# #
# # lblname = tk.Label(window, text="Name")
# # lblname.place(anchor="nw")
# # lblpwd = tk.Label(window, text="Password")
# # lblpwd.place(x=30, y = 90)
# #
# # btnsubmit = tk.Button(window, text="Submit")
# # btnsubmit.place(x=100,y =130)
# #
# # entname = tk.Entry(window, selectbackground="red", selectforeground="blue")
# # entname.place(x=100, y = 50)
# # entpwd = tk.Entry(window)
# # entpwd.place(x=100, y=90)
# #
# #
# # # using grid geometry manager
# # # lblname = tk.Label(window, text="Name")
# # # lblname.grid(row=0, column=0)
# # # lblpwd = tk.Label(window, text="Password")
# # # lblpwd.grid(row=1, column=0)
# # #
# # # btnsubmit = tk.Button(window, text="Submit")
# # # btnsubmit.grid(row=2, column=0)
# # #
# # # entname = tk.Entry(window)
# # # entname.grid(column=1, row=0)
# # # entpwd = tk.Entry(window)
# # # entpwd.grid(column=1, row=1 )
# #
# #
# # window.mainloop()
# #
# #
# #
# # #using place geometry method
# # # window = tk.Tk()
# # # window.geometry("450x300")
# # # window.title("tk")
# # #
# # # lbl_name = tk.Label(text=f"{'name'.title()}")
# # # lbl_email = tk.Label(text=f"{'email'.title()}")
# # # lbl_pwd = tk.Label(text=f"{'password'.title()}")
# # #
# # # ent_name = tk.Entry()
# # # ent_email = tk.Entry()
# # # ent_pwd = tk.Entry()
# # #
# # # ent_name.place(x=80, y=50)
# # # ent_email.place(x=80, y=90)
# # # ent_pwd.place(x=80, y=130)
# # #
# # # lbl_name.place(x=30, y=50)
# # # lbl_email.place(x=30, y=90)
# # # lbl_pwd.place(x=30, y=130)
# # #
# # # window.mainloop()