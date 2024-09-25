import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item.")

def print_item():
    selected_item = listbox.curselection()
    if selected_item:
        item = listbox.get(selected_item)
        messagebox.showinfo("Selected Item", f"You selected: {item}")
    else:
        messagebox.showwarning("Warning", "Please select an item.")

def delete_item():
    selected_item = listbox.curselection()
    if selected_item:
        listbox.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select an item to delete.")

# GUI setup
root = tk.Tk()
root.title("Listbox Example")

# Entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Listbox widget
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

print_button = tk.Button(root, text="Print Selected Item", command=print_item)
print_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Item", command=delete_item)
delete_button.pack(pady=5)

root.mainloop()
