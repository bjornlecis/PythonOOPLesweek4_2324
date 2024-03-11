import tkinter as tk

# Lijst met namen
namen = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eva",
    "Frank",
    "Grace",
    "Hannah",
    "Ian",
    "Julia"
]

# Functie om een naam toe te voegen aan de lijst
def voeg_naam_toe():
    nieuwe_naam = invoer.get()
    if nieuwe_naam:
        namen.append(nieuwe_naam)
        toon_namen()

# Functie om een naam te verwijderen uit de lijst
def verwijder_naam():
    geselecteerde_index = lijstbox.curselection()
    if geselecteerde_index:
        verwijderde_naam = namen.pop(geselecteerde_index[0])
        toon_namen()

# Functie om een naam in de lijst te wijzigen
def wijzig_naam():
    geselecteerde_index = lijstbox.curselection()
    if geselecteerde_index:
        nieuwe_naam = invoer.get()
        if nieuwe_naam:
            namen[geselecteerde_index[0]] = nieuwe_naam
            toon_namen()

# Functie om de namenlijst te sorteren van A-Z
def sorteer_namen():
    namen.sort()
    namen.reverse()
    toon_namen()

# Functie om de namenlijst op het scherm te tonen
def toon_namen():
    # Wis de huidige weergave van de namenlijst
    lijstbox.delete(0, tk.END)

    # Voeg alle namen toe aan de lijstbox
    for idx, naam in enumerate(namen):
        lijstbox.insert(tk.END, f"{idx+1}. {naam}")

# Creëer het hoofdvenster
venster = tk.Tk()
venster.title("Namenlijst")

# Maak een frame voor de lijst met namen
frame = tk.Frame(venster)
frame.pack(pady=10)

# Maak een lijstbox om de namen weer te geven
lijstbox = tk.Listbox(frame)
lijstbox.pack(side=tk.LEFT, padx=10)

# Voeg scrollen toe aan de lijstbox
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=lijstbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Koppel de scrollbar aan de lijstbox
lijstbox.config(yscrollcommand=scrollbar.set)

# Voeg een invoerveld toe om een nieuwe naam toe te voegen
invoer = tk.Entry(venster)
invoer.pack(pady=5)

# Voeg een knop toe om een nieuwe naam toe te voegen
toevoeg_knop = tk.Button(venster, text="Voeg naam toe", command=voeg_naam_toe)
toevoeg_knop.pack()

# Voeg een knop toe om een geselecteerde naam te verwijderen
verwijder_knop = tk.Button(venster, text="Verwijder geselecteerde naam", command=verwijder_naam)
verwijder_knop.pack()

# Voeg een knop toe om een geselecteerde naam te wijzigen
wijzig_knop = tk.Button(venster, text="Wijzig geselecteerde naam", command=wijzig_naam)
wijzig_knop.pack()

# Voeg een knop toe om de namenlijst te sorteren
sorteer_knop = tk.Button(venster, text="Sorteer namen", command=sorteer_namen)
sorteer_knop.pack()

# Toon de huidige lijst met namen
toon_namen()

# Start de mainloop
venster.mainloop()
