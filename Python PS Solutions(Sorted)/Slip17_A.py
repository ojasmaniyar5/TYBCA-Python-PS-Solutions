import tkinter as tk

def convert_to_uppercase():
    input_string = entry.get()
    uppercase_string = input_string.upper()
    result_label.config(text=uppercase_string)

# GUI setup
root = tk.Tk()
root.title("Uppercase Converter")

# Entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to convert to uppercase
convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
