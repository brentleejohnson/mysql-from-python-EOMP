from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Admin")
root.geometry("450x250")
root.config()

# Background Image
bg_img = PhotoImage(file="background3.png")
bg_img = bg_img.subsample(10)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=0, y=0)


# Buttons
# Users button
def display_users():
    root.destroy()
    import admin_users


users = Button(root, text="Display Users", command=display_users)
users.config(bg="#A4AC86", fg="#351C08", font=("Garuda", 15), cursor="hand2")
users.place(x=150, y=50)


# Kin Members button
def display_kin():
    root.destroy()
    import admin_kin


kin = Button(root, text="Display Users' 'Next of Kin'", command=display_kin)
kin.config(bg="#A4AC86", fg="#351C08", font=("Garuda", 15), cursor="hand2")
kin.place(x=90, y=150)


# Run the program
root.mainloop()
