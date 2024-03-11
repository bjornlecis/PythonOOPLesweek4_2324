import tkinter as tk

def change_color():
    selected_color = color_var.get()
    if selected_color == "Rood":
        root.configure(bg="red")
    elif selected_color == "Blauw":
        root.configure(bg="blue")
    elif selected_color == "Groen":
        root.configure(bg="green")
    elif selected_color == "Orange":
        root.configure(bg="orange")
    elif selected_color == "Paars":
        root.configure(bg="purple")

root = tk.Tk()
root.title("Achtergrondkleur kiezen")

colors = ["Rood", "Blauw", "Groen", "Orange", "Paars"]

color_var = tk.StringVar(root)
color_var.set(colors[2])

color_menu = tk.OptionMenu(root, color_var, *colors)
color_menu.pack(pady=10)

change_button = tk.Button(root, text="Verander Kleur", command=change_color)
change_button.pack(pady=5)

root.mainloop()