import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox
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

# Password
password_lbl = Label(root, text="Password", font=("Garuda", 15))
password_lbl.config(bg="#144552", fg="white")
password_lbl.place(x=90, y=360)

password_ent = Entry(root)
password_ent.config(bg="#144552", fg="white")
password_ent.place(x=280, y=375)

# Phone Number
phone_lbl = Label(root, text="Phone Number", font=("Garuda", 15))
phone_lbl.config(bg="#144552", fg="white")
phone_lbl.place(x=90, y=400)

phone_ent = Entry(root)
phone_ent.config(bg="#144552", fg="white")
phone_ent.place(x=280, y=415)

# ID Number
id_lbl = Label(root, text="ID Number", font=("Garuda", 15))
id_lbl.config(bg="#144552", fg="white")
id_lbl.place(x=90, y=440)

id_ent = Entry(root)
id_ent.config(bg="#144552", fg="white")
id_ent.place(x=280, y=455)


# Buttons
# Back button
def previous():
    root.destroy()
    import main


login_btn = Button(root, text="Back", command=previous)
login_btn.config(bg="#144552", fg="white")
login_btn.place(x=40, y=550)


# Register button
def register():
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="lifechoicesonline", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

    # Id No Validation
        if username_ent.get() == "" or password_ent.get() == "" or phone_ent.get() == "" or id_ent.get() == "":
            raise ValueError
        elif len(id_ent.get()) < 13 or len(id_ent.get()) > 13:
            messagebox.showerror(message="Id Number must be 13 digits")
        else:
            query1 = "insert into Users (username, password, phonenumber, idnumber) values ('{}', '{}', '{}', '{}')".format(username_ent.get(),
                                                                                                                            password_ent.get(),
                                                                                                                            phone_ent.get(),
                                                                                                                            id_ent.get())
            mycursor.execute(query1)
            mydb.commit()
            messagebox.showinfo(message="Registration complete. Proceed to sign-in")
            root.destroy()
            import next_of_kin

    except ValueError:
        messagebox.showerror("Error", "All Fields Are Required")


register_btn = Button(root, text="Register", command=register)
register_btn.config(bg="#144552", fg="white")
register_btn.place(x=240, y=550)


# Exit button
exit_btn = Button(root, text="Exit", command=exit)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=440, y=550)


# Run the program
root.mainloop()
