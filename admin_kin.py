import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Admin Kin Members")
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
mycursor.execute("select * from Next_of_kin")
users = mycursor.fetchall()
tree = ttk.Treeview(root)

# Define the number of columns
tree["columns"] = ("Name", "Phone", "Kin of")

# Formatting columns
tree.column("#0", width=75, minwidth=25)
tree.column("Name", anchor=CENTER)
tree.column("Phone", anchor=CENTER, width=120)
tree.column("Kin of", anchor=CENTER, width=150)

# Defining the column headings
tree.heading("#0", text="Labels", anchor=CENTER)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Phone", text="Phone #", anchor=CENTER)
tree.heading("Kin of", text="Kin of", anchor=CENTER)

# From the database
x = 0
for data in users:
    tree.insert(parent="", index="end", iid=x, text="User", values=(data[0], data[1], data[2]))
    x += 1

# Placing the treeview
tree.pack()


# Run the program
root.mainloop()
