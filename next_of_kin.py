import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Next of Kin")
root.geometry("700x750")
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

# Kin of
kin_lbl = Label(root, text="Kin of:", font=("Garuda", 20))
kin_lbl.config(bg="#184E77", fg="#B5E48C")
kin_lbl.place(x=315, y=500)

kin_ent = Entry(root)
kin_ent.config(bg="#D9ED92", fg="#184E77", font=("Garuda", 15))
kin_ent.place(x=240, y=580)


# Buttons
# Confirm button
def confirm():
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="lifechoicesonline", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if name_ent.get() == "" or phone_ent.get() == "" or kin_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=root)
        else:
            query1 = "insert into Next_of_kin (kin_name, kin_phone, kin_of) values ('{}', '{}', '{}')".format(name_ent.get(),
                                                                                                              phone_ent.get(),
                                                                                                              kin_ent.get())
            mycursor.execute(query1)
            mydb.commit()
            messagebox.showinfo(message="Registration complete. Proceed to sign-in")
            root.destroy()
            import main

    except ValueError:
        messagebox.showerror("Error", "Something went wrong!")


confirm_btn = Button(root, text="Confirm", font=("Garuda", 15), command=confirm)
confirm_btn.config(bg="#D9ED92", fg="#184E77")
confirm_btn.place(x=40, y=650)


# Exit button
def previous():
    root.destroy()
    import register


back_btn = Button(root, text="Back", font=("Garuda", 15), command=previous)
back_btn.config(bg="#D9ED92", fg="#184E77")
back_btn.place(x=590, y=650)


# Run the program
root.mainloop()
