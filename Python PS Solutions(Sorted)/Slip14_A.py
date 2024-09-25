import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        radius = float(radius_entry.get())
        height = float(height_entry.get())
        
        # Calculate surface area and volume
        surface_area = 2 * math.pi * radius * (radius + height)
        volume = math.pi * radius**2 * height
        
        # Display the results
        result = f"Surface Area: {surface_area:.2f}\nVolume: {volume:.2f}"
        messagebox.showinfo("Results", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Cylinder Calculator")

tk.Label(root, text="Radius:").pack()
radius_entry = tk.Entry(root)
radius_entry.pack()

tk.Label(root, text="Height:").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

root.mainloop()
