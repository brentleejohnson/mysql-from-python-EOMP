import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Admin")
root.geometry("700x600")
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
tree.column("Password", anchor=W, width=100)
tree.column("Phone", anchor=W, width=100)
tree.column("Id", anchor=W, width=130)

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

# Next_of_kin Table;
mydb2 = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database="lifechoicesonline", auth_plugin="mysql_native_password")

mycursor2 = mydb2.cursor()
mycursor2.execute("select * from Next_of_kin")
kin = mycursor2.fetchall()
tree2 = ttk.Treeview(root)

# Define the number of columns
tree2["columns"] = ("Name", "Phone #")

# Formatting columns
tree2.column("#0", width=75, minwidth=25)
tree2.column("Name", anchor=CENTER)
tree2.column("Phone #", anchor=W, width=100)

# Defining the column headings
tree2.heading("#0", text="Labels", anchor=CENTER)
tree2.heading("Username", text="Name", anchor=CENTER)
tree2.heading("Password", text="Phone #", anchor=CENTER)

# From the database
x = 0
for data in kin:
    tree2.insert(parent="", index="end", iid=x, text="User", values=(data[0], data[1], data[2]))
    x += 1

# Placing the treeview
tree.pack()
tree2.pack()


# Run the program
root.mainloop()
