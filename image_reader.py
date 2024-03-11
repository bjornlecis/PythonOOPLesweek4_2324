import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

original_image = None  # Define original_image as a global variable

def open_image():
    global original_image  # Declare original_image as a global variable
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo
        original_image = img  # Store the original image globally

def convert_to_grayscale():
    global original_image  # Declare original_image as a global variable
    if original_image:
        grayscale_img = original_image.convert("L")
        grayscale_photo = ImageTk.PhotoImage(grayscale_img)
        canvas.delete("all")  # Clear canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=grayscale_photo)
        canvas.image = grayscale_photo

# Create the main window
window = tk.Tk()
window.title("Image Uploader")
window.geometry("400x400")

# Create a canvas
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack(fill=tk.BOTH, expand=True)

# Button to open image
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Button to convert to grayscale
grayscale_button = tk.Button(window, text="Convert to Grayscale", command=convert_to_grayscale)
grayscale_button.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
