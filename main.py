# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Registration")
root.geometry("550x350")
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
title_lbl.config(bg="#212F45", fg="white")
title_lbl.pack()

# Name
name_lbl = Label(root, text="Name", font=("Garuda", 15))
name_lbl.config(bg="#272640", fg="white")
name_lbl.place(x=90, y=70)

name_ent = Entry(root)
name_ent.config(bg="#B7E4C7", fg="black")
name_ent.place(x=280, y=80)

# Surname
surname_lbl = Label(root, text="Surname", font=("Garuda", 15))
surname_lbl.config(bg="#3E1F47", fg="white")
surname_lbl.place(x=90, y=110)

surname_ent = Entry(root)
surname_ent.config(bg="#B7E4C7", fg="black")
surname_ent.place(x=280, y=120)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 15))
phone_lbl.config(bg="#1B3A4B", fg="white")
phone_lbl.place(x=90, y=150)

phone_ent = Entry(root)
phone_ent.config(bg="#B7E4C7", fg="black")
phone_ent.place(x=280, y=160)

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#006466", fg="white")
id_lbl.place(x=90, y=190)

id_ent = Entry(root)
id_ent.config(bg="#B7E4C7", fg="black")
id_ent.place(x=280, y=200)

# Buttons
register_btn = Button(root, text="Register")
register_btn.config(bg="#B7E4C7", fg="black")
register_btn.place(x=40, y=300)

exit_btn = Button(root, text="Exit", command=exit)
exit_btn.config(bg="#B7E4C7", fg="black")
exit_btn.place(x=440, y=300)


# Run the program
root.mainloop()
