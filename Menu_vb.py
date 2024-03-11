import tkinter as tk

def change_background_color(color):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("200x200")
    new_window.configure(background=color)


def create_menu():
    menubar = tk.Menu(root)
    color_menu = tk.Menu(menubar, tearoff=0)
    color_menu.add_command(label="Blue", command=lambda: change_background_color("blue"))
    color_menu.add_command(label="Red", command=lambda: change_background_color("red"))
    color_menu.add_command(label="Green", command=lambda: change_background_color("green"))
    color_menu.add_command(label="Pink", command=lambda: change_background_color("pink"))
    color_menu.add_command(label="Orange", command=lambda: change_background_color("orange"))
    menubar.add_cascade(label="Colors", menu=color_menu)
    root.config(menu=menubar)

root = tk.Tk()
root.title("Color Chooser")
root.geometry("400x300")

create_menu()

root.mainloop()