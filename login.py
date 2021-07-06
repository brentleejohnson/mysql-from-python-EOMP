from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Logging In/Out")
root.geometry("550x400")
root.config(bg="#081C15")
# root.wm_attributes('-type', 'black')

# Background Image
bg_img = PhotoImage(file="background.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=0, y=0)

# Details
# Life Choices Academy Logo
lifechoices_logo = PhotoImage(file="lifechoiceslogo.png")
lifechoices_logo = lifechoices_logo.subsample(2)
lifechoices_logo_lbl = Label(root, image=lifechoices_logo, width=400, height=150)
lifechoices_logo_lbl.config(bg="black")
lifechoices_logo_lbl.pack()

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#144552", fg="white")
id_lbl.place(x=90, y=200)

id_ent = Entry(root)
id_ent.config(bg="#144552", fg="white")
id_ent.place(x=280, y=215)

# Buttons
register_btn = Button(root, text="Log In")
register_btn.config(bg="#144552", fg="white")
register_btn.place(x=40, y=330)

login_btn = Button(root, text="Log Out")
login_btn.config(bg="#144552", fg="white")
login_btn.place(x=250, y=330)

# Exit button
exit_btn = Button(root, text="Exit", command=exit)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=440, y=330)


# Run the program
root.mainloop()
