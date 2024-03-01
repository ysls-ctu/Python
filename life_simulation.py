import random
import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.happiness = 100
        self.wealth = 100
        self.age = 0

    def increment_age(self):
        self.age += 1

    def work(self):
        self.wealth += random.randint(10, 20)
        self.happiness -= random.randint(1, 5)
        self._check_random_event()

    def play(self):
        self.happiness += random.randint(10, 20)
        self.wealth -= random.randint(1, 5)
        self._check_random_event()

    def sleep(self):
        self.health += random.randint(10, 20)
        self.happiness += random.randint(5, 10)
        self._check_random_event()

    def _check_random_event(self):
        if random.random() < 0.1:  # 10% chance of illness
            self.health -= random.randint(10, 20)
            messagebox.showinfo("Random Event", "You fell ill!")
        if random.random() < 0.1:  # 10% chance of a windfall
            self.wealth += random.randint(50, 100)
            messagebox.showinfo("Random Event", "You received a windfall!")
        if random.random() < 0.1:  # 10% chance of a windfall
            self.health += random.randint(50, 100)
            messagebox.showinfo("Random Event", "A cow mauled you!")
        if random.random() < 0.1:  # 10% chance of a windfall
            self.health += random.randint(50, 100)
            messagebox.showinfo("Random Event", "You're strucked by a lightning!'")
        if random.random() < 0.1:  # 10% chance of a windfall
            self.wealth += random.randint(50, 100)
            messagebox.showinfo("Random Event", "You met a genie!")

    def status(self):
        return f"Name: {self.name}\nAge: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}\nWealth: {self.wealth}"

def handle_work():
    player.work()
    update_ui()

def handle_play():
    player.play()
    update_ui()

def handle_sleep():
    player.sleep()
    update_ui()

def handle_age():
    player.increment_age()
    update_ui()

def update_ui():
    age_label.config(text=f"Age: {player.age}")
    health_label.config(text=f"Health: {player.health}")
    happiness_label.config(text=f"Happiness: {player.happiness}")
    wealth_label.config(text=f"Wealth: {player.wealth}")


def start_game():
    name = name_entry.get()
    if name:
        global player
        player = Person(name)
        name_entry.destroy()
        start_button.destroy()
        show_game_ui()
    else:
        messagebox.showerror("Error", "Please enter your name.")

root = tk.Tk()
root.title("Life Simulator")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

age_label = tk.Label(root, text="")
health_label = tk.Label(root, text="")
happiness_label = tk.Label(root, text="")
wealth_label = tk.Label(root, text="")

age_button = tk.Button(root, text="Age", command=handle_age)
work_button = tk.Button(root, text="Work", command=handle_work)
play_button = tk.Button(root, text="Play", command=handle_play)
sleep_button = tk.Button(root, text="Sleep", command=handle_sleep)



def show_game_ui():
    age_label.pack()
    health_label.pack()
    happiness_label.pack()
    wealth_label.pack()
    age_button.pack()
    work_button.pack()
    play_button.pack()
    sleep_button.pack()

    update_ui()

root.mainloop()


# research environment and research procedure

# def to_last_row():
#     import openpyxl

#     workbook = openpyxl.load_workbook('c:\\Users\\User.DESKTOP-FC21VHI\\Documents\\SOS - SalasY 1217\\BDG.xlsx')


#     sheet = workbook.active

#     last_row = sheet.max_row

#     last_value = sheet.cell(row = last_row, column = 1).value

#     while last_value == "" and last_row > 1:
#         last_row -= 1
#         last_value = sheet.cell(row = last_row, column = 1).value
    
#     sheet.cell(row = last_row, column = 1).coordinate

#     workbook.save('c:\\Users\\User.DESKTOP-FC21VHI\\Documents\\SOS - SalasY 1217\\BDG - Updated.xlsx')

# to_last_row()


