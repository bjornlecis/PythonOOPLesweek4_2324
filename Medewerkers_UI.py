from Medewerkers import medewerkers
import tkinter as tk
from tkinter import ttk

# Functie om de voornamen van medewerkers op te halen
def get_voornamen():
    voornamen = [medewerker.voornaam for medewerker in medewerkers]
    return voornamen
def toon_attributen(event):
    geselecteerde_voornaam = selected_voornaam.get()
    for widget in frame.winfo_children():
        widget.destroy()  # Vernietig alle widgets in het frame, behalve de dropdownlist
    for medewerker in medewerkers:
        if medewerker.voornaam == geselecteerde_voornaam:
            for key, value in vars(medewerker).items():
                label = tk.Label(frame, text=f"{key.capitalize()}: {value}")
                label.pack()

# Tkinter applicatie
root = tk.Tk()
root.title("Medewerker Informatie")

# Dropdownlist
voornamen = get_voornamen()
selected_voornaam = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_voornaam, values=voornamen)
dropdown.bind("<<ComboboxSelected>>", toon_attributen)
dropdown.pack(pady=10)

# Frame voor labels met attributen
frame = tk.Frame(root)
frame.pack(pady=10)

# Start de Tkinter main loop
root.mainloop()

