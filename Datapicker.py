import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today().date()
    if birthdate.year > today.year:
        birthdate = birthdate.replace(year=birthdate.year - 100)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def show_selected_date():
    birthdate = cal.get_date()
    age = calculate_age(birthdate)
    messagebox.showinfo("Age", f"Your age is {age} years.")

root = tk.Tk()
root.title("Birthday Date Picker")

# Create a DateEntry widget
cal = DateEntry(root, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

# Button to show selected date
select_button = tk.Button(root, text="Show Age", command=show_selected_date)
select_button.pack(pady=5)

root.mainloop()
