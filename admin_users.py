import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Admin Users Page")
root.geometry("800x600")
root.config()

# Background Image
bg_img = PhotoImage(file="background3.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=0, y=0)

# Users Table;
mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database="lifechoicesonline", auth_plugin="mysql_native_password")

mycursor = mydb.cursor()
mycursor.execute("select * from Users")
users = mycursor.fetchall()
tree = ttk.Treeview(root)

# Define the number of columns
tree["columns"] = ("Username", "Password", "Phone", "Id")

# Formatting columns
tree.column("#0", width=75, minwidth=25)
tree.column("Username", anchor=CENTER)
tree.column("Password", anchor=CENTER, width=160)
tree.column("Phone", anchor=CENTER, width=150)
tree.column("Id", anchor=CENTER, width=150)

# Defining the column headings
tree.heading("#0", text="Labels", anchor=CENTER)
tree.heading("Username", text="Username", anchor=CENTER)
tree.heading("Password", text="Password", anchor=CENTER)
tree.heading("Phone", text="Phone #", anchor=CENTER)
tree.heading("Id", text="ID #", anchor=CENTER)

# From the database
x = 0
for data in users:
    tree.insert(parent="", index="end", iid=x, text="User", values=(data[0], data[1], data[2], data[3]))
    x += 1

# Placing the treeview
tree.pack()


# Run the program
root.mainloop()
