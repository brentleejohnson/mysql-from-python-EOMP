# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Registration")
root.geometry("500x300")
root.config(bg="#081C15")

# Background Image
# bg_img = PhotoImage(file="background.jpg")
# bg_img_lbl = Label(root, img=bg_img)
# bg_img_lbl.pack()

# Register Details
# Name
name_lbl = Label(root, text="Name")
name_lbl.config()
name_lbl.place()

name_ent = Entry(root)
name_ent.config()
name_ent.pack()

# Surname
surname_lbl = Label(root, text="Surname")
surname_lbl.config()
surname_lbl.pack()

surname_ent = Entry(root)
surname_ent.config()
surname_ent.pack()

# Phone Number
# ID Number


# Run the program
root.mainloop()
