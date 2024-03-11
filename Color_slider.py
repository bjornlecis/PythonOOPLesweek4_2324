import tkinter as tk

def update_color(dummy_arg=None):
    # Get the current values of the sliders
    red_value = red_slider.get()
    green_value = green_slider.get()
    blue_value = blue_slider.get()

    # Construct the hexadecimal color code
    color_code = f'#{red_value:02x}{green_value:02x}{blue_value:02x}'

    # Update the background color of the frame
    color_frame.config(bg=color_code)

# Create the main window
window = tk.Tk()
window.title("Color Slider")
window.geometry("300x200")

# Create a frame to fill the window for color display
color_frame = tk.Frame(window, width=300, height=200)
color_frame.pack()

# Create sliders for red, green, and blue
red_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=update_color)
red_slider.pack(pady=10)
green_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=update_color)
green_slider.pack(pady=10)
blue_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=update_color)
blue_slider.pack(pady=10)

# Initial color update
update_color()

# Start the Tkinter event loop
window.mainloop()
