from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("Next of Kin")
root.geometry("700x600")
root.config()

# Background Image
bg_img = PhotoImage(file="background2.png")
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

# Name
name_lbl = Label(root, text="Name", font=("Garuda", 15))
name_lbl.config(bg="#144552", fg="white")
name_lbl.place(x=250, y=210)

name_ent = Entry(root)
name_ent.config(bg="#144552", fg="white")
name_ent.place(x=350, y=225)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 15))
phone_lbl.config(bg="#144552", fg="white")
phone_lbl.place(x=175, y=280)

phone_ent = Entry(root)
phone_ent.config(bg="#144552", fg="white")
phone_ent.place(x=350, y=295)

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#144552", fg="white")
id_lbl.place(x=215, y=350)

id_ent = Entry(root)
id_ent.config(bg="#144552", fg="white")
id_ent.place(x=350, y=365)


# Buttons
# Confirm button
def confirm():
    root.destroy()
    import login


confirm_btn = Button(root, text="Confirm", font=("Garuda", 15), command=confirm)
confirm_btn.config(bg="#144552", fg="white")
confirm_btn.place(x=40, y=500)


# Exit button
def previous():
    root.destroy()
    import main


exit_btn = Button(root, text="Exit", font=("Garuda", 15), command=previous)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=600, y=500)


# Run the program
root.mainloop()
