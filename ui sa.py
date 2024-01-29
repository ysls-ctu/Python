import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class SAProcess:
    def __init__(self, root):
        self.root = root
        self.root.title("Reports Processor")
        self.root.geometry("400x300")  # fixed width and height for the window
        self.root.configure(bg="#f0f0f0")

        # Disable window resizing
        self.root.resizable(False, False)

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        custom_font = ("Arial", 10)  # Decrease the font size

        self.select_file_button = ttk.Button(self.frame, text="Select File", command=self.select_file, style="TButton", width=20)
        self.select_file_button.pack(pady=10, anchor="center")

        self.selected_file_label = ttk.Label(self.frame, text="", font=custom_font, wraplength=350)  
        self.selected_file_label.pack(pady=5)

        self.process1_button = ttk.Button(self.frame, text="Day Sales Process", style="TButton", width=20)
        self.process1_button.pack(pady=5, anchor="center")

        self.process2_button = ttk.Button(self.frame, text="Process 2", style="TButton", width=20)
        self.process2_button.pack(pady=5, anchor="center")

        self.process3_button = ttk.Button(self.frame, text="Process 3", style="TButton", width=20)
        self.process3_button.pack(pady=5, anchor="center")

        style = ttk.Style()
        style.configure("TButton", font=custom_font)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            self.selected_file_label.config(text=file_path)  # Update the label with the selected file path

# main window run
root = tk.Tk()
app = SAProcess(root)
root.mainloop()


