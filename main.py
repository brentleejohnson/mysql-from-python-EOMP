# Brent Lee Johnson - Class 1
# MySQL With Python - EOMP


import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


root = tk.Tk()
root.title("Logging In/Out")
root.geometry("550x500")
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


# Register button
def Register():
    root.destroy()
    import register


register_btn = Button(root, text="Not Registered?", cursor="hand2", command=Register)
register_btn.config(bg="#144552", fg="white", bd="0", font=("Garuda", 10))
register_btn.pack()

# Username
username_lbl = Label(root, text="Username", font=("Garuda", 15))
username_lbl.config(bg="#144552", fg="white")
username_lbl.place(x=90, y=260)

username_ent = Entry(root)
username_ent.config(bg="#144552", fg="white")
username_ent.place(x=280, y=275)

# Password
password_lbl = Label(root, text="Password", font=("Garuda", 15))
password_lbl.config(bg="#144552", fg="white")
password_lbl.place(x=92, y=320)

password_ent = Entry(root)
password_ent.config(bg="#144552", fg="white")
password_ent.place(x=280, y=335)


# Buttons
# Log In Button
def login():
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                               database="lifechoicesonline", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if username_ent.get() == "" or password_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            mycursor.execute('select * from Users where username=%s and password=%s',
                             (username_ent.get(), password_ent.get()))

            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username And Password")
            else:
                messagebox.showinfo(message="Login Successful! Enjoy Your Day!")
                root.destroy()
    except ValueError:
        messagebox.showerror("Error", "Something went wrong")


login_btn = Button(root, text="Log In", cursor="hand2", command=login)
login_btn.config(bg="#144552", fg="white")
login_btn.place(x=50, y=430)


# Log Out Button
def logout():
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                               database="lifechoicesonline", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if username_ent.get() == "" or password_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            mycursor.execute('select * from Users where username=%s and password=%s',
                             (username_ent.get(), password_ent.get()))

            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username And Password")
            else:
                messagebox.showinfo(message="Logout Successful! Enjoy Your Day!")
                root.destroy()
    except ValueError:
        messagebox.showerror("Error", "Something went wrong")


logout_btn = Button(root, text="Log Out", cursor="hand2", command=logout)
logout_btn.config(bg="#144552", fg="white")
logout_btn.place(x=240, y=430)

# Exit button
exit_btn = Button(root, text="Exit", cursor="hand2", command=exit)
exit_btn.config(bg="#144552", fg="white")
exit_btn.place(x=440, y=430)


# Run the program
root.mainloop()
