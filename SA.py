import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd

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

        self.process1_button = ttk.Button(self.frame, text="Day Sales Process", style="TButton", width=20, command=self.process1)
        self.process1_button.pack(pady=5, anchor="center")

        self.process2_button = ttk.Button(self.frame, text="Process 2", style="TButton", width=20, command=self.process2)
        self.process2_button.pack(pady=5, anchor="center")

        self.process3_button = ttk.Button(self.frame, text="Process 3", style="TButton", width=20, command=self.process3)
        self.process3_button.pack(pady=5, anchor="center")

        style = ttk.Style()
        style.configure("TButton", font=custom_font)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            self.selected_file_label.config(text=file_path)  # Update the label with the selected file path

    def process1(self):
        file_path = self.selected_file_label.cget("text")
        if not file_path:
            return  # No file selected

        try:
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Remove columns D to N and columns Q to V
            columns_to_remove = ['SKU', 'Sessions - Total', 'Sessions - Total - B2B', 'Session Percentage - Total',
                                'Session Percentage - Total - B2B', 'Page Views - Total', 'Page Views - Total - B2B',
                                'Page Views Percentage - Total', 'Page Views Percentage - Total - B2B',
                                'Featured Offer (Buy Box) Percentage', 'Featured Offer (Buy Box) Percentage - B2B',
                                'Unit Session Percentage', 'Unit Session Percentage - B2B', 'Ordered Product Sales',
                                'Ordered Product Sales - B2B', 'Total Order Items', 'Total Order Items - B2B']

            df = df.drop(columns=columns_to_remove, axis=1)

            # Move columns O and P right of column C
            df.insert(3, 'Units Ordered', df.pop('Units Ordered'))
            df.insert(4, 'Units Ordered - B2B', df.pop('Units Ordered - B2B'))

            # Save the modified DataFrame to a new CSV file
            new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if new_file_path:
                df.to_csv(new_file_path, index=False)
                messagebox.showinfo("Success", "Processing complete. New file saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")




    def process2(self):
        # Add your logic for the second process
        pass

    def process3(self):
        # Add your logic for the third process
        pass

# main window run
root = tk.Tk()
app = SAProcess(root)
root.mainloop()
