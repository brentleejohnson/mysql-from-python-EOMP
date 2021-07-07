# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Registration")
root.geometry("550x600")
root.config(bg="#081C15")
# root.wm_attributes('-type', 'black')

# Background Image
bg_img = PhotoImage(file="background.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=0, y=0)

# Register Details
# Title
title_lbl = Label(root, text="Registration", font=("Garuda", 18))
title_lbl.config(bg="white", fg="#144552")
title_lbl.pack()

# Life Choices Academy Logo
lifechoices_logo = PhotoImage(file="lifechoiceslogo.png")
lifechoices_logo = lifechoices_logo.subsample(2)
lifechoices_logo_lbl = Label(root, image=lifechoices_logo, width=400, height=150)
lifechoices_logo_lbl.config(bg="black")
lifechoices_logo_lbl.place(x=75, y=100)

# Username
username_lbl = Label(root, text="Username", font=("Garuda", 15))
username_lbl.config(bg="#144552", fg="white")
username_lbl.place(x=90, y=320)

username_ent = Entry(root)
username_ent.config(bg="#144552", fg="white")
username_ent.place(x=280, y=335)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 15))
phone_lbl.config(bg="#144552", fg="white")
phone_lbl.place(x=90, y=360)

phone_ent = Entry(root)
phone_ent.config(bg="#144552", fg="white")
phone_ent.place(x=280, y=375)

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#144552", fg="white")
id_lbl.place(x=90, y=400)

id_ent = Entry(root)
id_ent.config(bg="#144552", fg="white")
id_ent.place(x=280, y=415)


# Buttons
# Register button
def register():
    root.destroy()
    import next_of_kin


register_btn = Button(root, text="Register", command=register)
register_btn.config(bg="#144552", fg="white")
register_btn.place(x=40, y=550)


# Login
def login():
    root.destroy()
    import login


login_btn = Button(root, text="Login", command=login)
login_btn.config(bg="#144552", fg="white")
login_btn.place(x=250, y=550)

# Exit button
exit_btn = Button(root, text="Exit", command=exit)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=440, y=550)


# Run the program
root.mainloop()
