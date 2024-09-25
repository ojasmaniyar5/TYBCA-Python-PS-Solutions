import tkinter as tk
from tkinter import font

def change_font():
    font_name = font_name_entry.get()
    font_size = int(font_size_entry.get())
    is_bold = bold_var.get()
    
    style = 'bold' if is_bold else 'normal'
    new_font = (font_name, font_size, style)
    label.config(font=new_font)

# GUI setup
root = tk.Tk()
root.title("Change Label Font")

# Create label
label = tk.Label(root, text="Sample Text", font=("Arial", 16))
label.pack(pady=10)

# Font name entry
tk.Label(root, text="Font Name:").pack()
font_name_entry = tk.Entry(root)
font_name_entry.insert(0, "Arial")
font_name_entry.pack()

# Font size entry
tk.Label(root, text="Font Size:").pack()
font_size_entry = tk.Entry(root)
font_size_entry.insert(0, "16")
font_size_entry.pack()

# Bold checkbox
bold_var = tk.BooleanVar()
tk.Checkbutton(root, text="Bold", variable=bold_var).pack()

# Button to apply changes
tk.Button(root, text="Change Font", command=change_font).pack(pady=10)

root.mainloop()
