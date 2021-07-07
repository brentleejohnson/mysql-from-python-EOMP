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
name_lbl = Label(root, text="Name", font=("Garuda", 20))
name_lbl.config(bg="#184E77", fg="#B5E48C")
name_lbl.place(x=315, y=180)

name_ent = Entry(root)
name_ent.config(bg="#D9ED92", fg="#184E77", font=("Garuda", 15))
name_ent.place(x=240, y=260)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 20))
phone_lbl.config(bg="#184E77", fg="#B5E48C")
phone_lbl.place(x=260, y=340)

phone_ent = Entry(root)
phone_ent.config(bg="#D9ED92", fg="#184E77", font=("Garuda", 15))
phone_ent.place(x=240, y=430)


# Buttons
# Confirm button
def confirm():
    root.destroy()
    import login


confirm_btn = Button(root, text="Confirm", font=("Garuda", 15), command=confirm)
confirm_btn.config(bg="#D9ED92", fg="#184E77")
confirm_btn.place(x=40, y=500)


# Exit button
def previous():
    root.destroy()
    import main


exit_btn = Button(root, text="Exit", font=("Garuda", 15), command=previous)
exit_btn.config(bg="#D9ED92", fg="#184E77")
exit_btn.place(x=600, y=500)


# Run the program
root.mainloop()
