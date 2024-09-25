import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def check_number():
    try:
        n = int(entry.get())
        option = var.get()
        if option == 1:
            result = "Prime" if is_prime(n) else "Not Prime"
        elif option == 2:
            result = "Perfect" if is_perfect(n) else "Not Perfect"
        elif option == 3:
            result = "Armstrong" if is_armstrong(n) else "Not Armstrong"
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# GUI setup
root = tk.Tk()
root.title("Number Checker")

tk.Label(root, text="Enter a number:").pack()
entry = tk.Entry(root)
entry.pack()

var = tk.IntVar()

# Radio buttons for Prime, Perfect, Armstrong
tk.Radiobutton(root, text="Prime", variable=var, value=1).pack()
tk.Radiobutton(root, text="Perfect", variable=var, value=2).pack()
tk.Radiobutton(root, text="Armstrong", variable=var, value=3).pack()

# Check button
tk.Button(root, text="Check", command=check_number).pack()

root.mainloop()
