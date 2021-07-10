from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Admin Login Page")
root.geometry("500x650")
root.config()

# Background Image
bg_img = PhotoImage(file="background2.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=0, y=0)

# Life Choices Academy Logo
lifechoices_logo = PhotoImage(file="lifechoiceslogo.png")
lifechoices_logo = lifechoices_logo.subsample(2)
lifechoices_logo_lbl = Label(root, image=lifechoices_logo, width=400, height=150)
lifechoices_logo_lbl.config(bg="black")
lifechoices_logo_lbl.pack()

# Details
# Title
title_lbl = Label(root, text="Welcome to the Admin Page", font=("Garuda", 15))
title_lbl.config(bg="#184E77", fg="#B5E48C")
title_lbl.pack()

# Username
user_lbl = Label(root, text="Username", font=("Garuda", 15))
user_lbl.config(bg="#184E77", fg="#B5E48C")
user_lbl.place(x=80, y=280)

user_ent = Entry(root, font=("Garuda", 15))
user_ent.config(bg="#D9ED92", fg="#184E77")
user_ent.place(x=240, y=280)

# Password
password_lbl = Label(root, text="Password", font=("Garuda", 15))
password_lbl.config(bg="#184E77", fg="#B5E48C")
password_lbl.place(x=82, y=400)

password_ent = Entry(root, font=("Garuda", 15))
password_ent.config(bg="#D9ED92", fg="#184E77")
password_ent.place(x=240, y=400)


# Buttons
# Login button
def login():
    try:
        if user_ent.get() == "" or password_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=root)
        elif user_ent.get() == "admin21" and password_ent.get() == "adminonline1234":
            messagebox.showinfo(message="Logged in!")
            root.destroy()
            import admin
    except ValueError:
        messagebox.showerror("Error", "Oops! Something went wrong")


login_btn = Button(root, text="Login", font=("Garuda", 15), command=login)
login_btn.config(bg="#D9ED92", fg="#184E77", cursor="hand2")
login_btn.place(x=120, y=580)


# Exit button
def exit():
    root.destroy()
    import main


exit_btn = Button(root, text="Exit", font=("Garuda", 15), command=exit)
exit_btn.config(bg="#D9ED92", fg="#184E77", cursor="hand2")
exit_btn.place(x=310, y=580)


# Run the program
root.mainloop()
