# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Registration")
root.geometry("550x350")
root.config(bg="#081C15")

# Background Image
# bg_img = PhotoImage(file="background.jpg")
# bg_img_lbl = Label(root, img=bg_img)
# bg_img_lbl.pack()

# Register Details
# Title
title_lbl = Label(root, text="Registration", font=("Garuda", 18))
title_lbl.config(bg="#74C69D", fg="#081C15")
title_lbl.pack()

# Name
name_lbl = Label(root, text="Name", font=("Garuda", 15))
name_lbl.config(bg="#081C15", fg="#74C69D")
name_lbl.place(x=90, y=70)

name_ent = Entry(root)
name_ent.config(bg="#B7E4C7", fg="#081C15")
name_ent.place(x=280, y=80)

# Surname
surname_lbl = Label(root, text="Surname", font=("Garuda", 15))
surname_lbl.config(bg="#081C15", fg="#74C69D")
surname_lbl.place(x=90, y=110)

surname_ent = Entry(root)
surname_ent.config(bg="#B7E4C7", fg="#081C15")
surname_ent.place(x=280, y=120)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 15))
phone_lbl.config(bg="#081C15", fg="#74C69D")
phone_lbl.place(x=90, y=150)

phone_ent = Entry(root)
phone_ent.config(bg="#B7E4C7", fg="#081C15")
phone_ent.place(x=280, y=160)

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#081C15", fg="#74C69D")
id_lbl.place(x=90, y=190)

id_ent = Entry(root)
id_ent.config(bg="#B7E4C7", fg="#081C15")
id_ent.place(x=280, y=200)

# Buttons
register_btn = Button(root, text="Register")
register_btn.config(bg="#B7E4C7", fg="#081C15")
register_btn.place(x=440, y=300)


# Run the program
root.mainloop()
