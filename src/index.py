import json
import os
import tkinter as tk
import easygui
from PIL import ImageTk


def tutorial():
    welcome = ImageTk.PhotoImage(file="..\\images\\welcome.png")
    welcome_label = tk.Label(window, width=700, height=380, image=welcome)
    welcome_label.place(x=150, y=20)
    login_button = tk.Button(window, width=10, height=5, text="login")
    login_button.place(x=150, y=500)
    tip1 = tk.Label(window, width=20, height=5, text="Have an account? Login!")
    tip1.place(x=150, y=410)
    regist_button = tk.Button(window, width=10, height=5, text="registser")
    regist_button.place(x=500, y=500)
    tip2 = tk.Label(window, width=30, height=5, text="Don't have an account? Registser!")
    tip2.place(x=500, y=410)
    window.resizable(0, 0)
    window.geometry("1000x800")
    window.mainloop()


check = os.listdir("../settings")
# data recovery
if len(check) == 0:
    with open("..\\backup\\default_settings.json", mode='r', encoding='utf-8') as f:
        backup_data = f.read()
    with open("..\\settings\\default_settings.json", mode="w", encoding="utf-8") as f:
        f.write(backup_data)
    with open("..\\backup\\user.json", mode='r', encoding='utf-8') as f:
        backup_data = f.read()
    with open("..\\settings\\user.json", mode="w", encoding="utf-8") as f:
        f.write(backup_data)
    with open("..\\backup\\user_settings.json", mode='r', encoding='utf-8') as f:
        backup_data = f.read()
    with open("..\\settings\\user_settings.json", mode="w", encoding="utf-8") as f:
        f.write(backup_data)
# import data
with open("..\\settings\\default_settings.json", mode='r', encoding='utf-8') as f:
    default_settings = json.load(f)
with open("..\\settings\\user_settings.json", mode='r', encoding='utf-8') as f:
    user_settings = json.load(f)
print(user_settings)
program_name = user_settings["program_name"]
print(program_name)
with open("..\\settings\\user.json", mode='r', encoding='utf-8') as f:
    user = json.load(f)
window = tk.Tk()
print(user)
# check if the user is new
if user["login_date"] == 0:
    print('tutorial()')
    tutorial()
window.title('"' + str(program_name) + '"')
window.mainloop()
