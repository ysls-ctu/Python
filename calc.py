import tkinter as tk
from tkinter import ttk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# main window
window = tk.Tk()
window.title("Calculator")

# minimum and maximum sizes
window.minsize(int(window.winfo_screenwidth() * 0.1), int(window.winfo_screenheight() * 0.2))
window.maxsize(int(window.winfo_screenwidth() * 0.3), int(window.winfo_screenheight() * 0.4))

# initial size
initial_width = int(window.winfo_screenwidth() * 0.2)
initial_height = int(window.winfo_screenheight() * 0.3)
window.geometry(f"{initial_width}x{initial_height}")

entry = ttk.Entry(window, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")

# Style
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(window, text=button, style='TButton',
               command=lambda b=button: on_button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, pady=5, padx=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
ttk.Button(window, text='C', style='TButton', command=clear_entry).grid(row=row_val, column=col_val, pady=5, padx=5, sticky="nsew")

# responsiveness
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# event loop
window.mainloop()
