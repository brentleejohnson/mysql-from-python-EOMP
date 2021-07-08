# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Logging In/Out")
root.geometry("550x450")
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

# Username
username_lbl = Label(root, text="Username", font=("Garuda", 15))
username_lbl.config(bg="#144552", fg="white")
username_lbl.place(x=90, y=210)

username_ent = Entry(root)
username_ent.config(bg="#144552", fg="white")
username_ent.place(x=280, y=225)

# Password
password_lbl = Label(root, text="Password", font=("Garuda", 15))
password_lbl.config(bg="#144552", fg="white")
password_lbl.place(x=92, y=270)

password_ent = Entry(root)
password_ent.config(bg="#144552", fg="white")
password_ent.place(x=280, y=285)

# Buttons
# Log In Button
login_btn = Button(root, text="Log In", cursor="hand2")
login_btn.config(bg="#144552", fg="white")
login_btn.place(x=50, y=380)

# Log Out Button
logout_btn = Button(root, text="Log Out")
logout_btn.config(bg="#144552", fg="white")
logout_btn.place(x=240, y=380)

# Exit button
exit_btn = Button(root, text="Exit", command=exit)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=440, y=380)


# Run the program
root.mainloop()
