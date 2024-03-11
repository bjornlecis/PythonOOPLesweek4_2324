import tkinter as tk
from tkinter import messagebox


def plus():
    getal1 = int(string_getal1.get())
    getal2 = int(string_getal2.get())
    som = str(getal1 + getal2)
    string_uitkomst.set(som)
    messagebox.showinfo("De som is", som)
def maal():
    getal1 = int(string_getal1.get())
    getal2 = int(string_getal2.get())
    uitkomt = str(getal1 * getal2)
    string_uitkomst.set(uitkomt)
    messagebox.showinfo("het product is", uitkomt)
def grootste():
    getal1 = int(string_getal1.get())
    getal2 = int(string_getal2.get())
    if getal1 > getal2:
        uitkomst = f"{getal1} is het grootst"
    elif getal2 > getal1:
        uitkomst = f"{getal2} is het grootst"
    else:
        uitkomst = "getallen zijn even groot"

    string_uitkomst.set(uitkomst)
    messagebox.showinfo("het product is", uitkomst)


root = tk.Tk()
string_getal1 = tk.StringVar()
string_getal2 = tk.StringVar()
string_uitkomst = tk.StringVar()
root.geometry("400x400")
lbl_getal1 = tk.Label(root, text="Getal1", foreground="#FF0FF0").grid(row=0, column=0)
txt_getal1 = tk.Entry(root, textvariable=string_getal1).grid(row=0, column=1)
lbl_getal2 = tk.Label(root, text="Getal2", foreground="Blue").grid(row=1, column=0)
txt_getal2 = tk.Entry(root, textvariable=string_getal2).grid(row=1, column=1)
btn_bevestig = tk.Button(text="+", command=plus).grid(row=1, column=2)
btn_bevestig = tk.Button(text="x", command=maal).grid(row=1, column=3)
btn_bevestig = tk.Button(text="grootst", command=grootste).grid(row=1, column=4)
lbl_uitkomst = tk.Label(root, textvariable=string_uitkomst).grid(row=2, column=0)
root.mainloop()

