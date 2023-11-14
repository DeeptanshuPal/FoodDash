from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as con
from ExistingUser import *
from NewUser import *

#Checking if MySQL DataBase "FoodDashDB" exists, if yes: connect to that database, else: create the database.

#If we have to create the database, then add the following tables into the database:
#   'CustomerData' with columns uname, pass, name, mob, address.
#   'Evergreen' with columns MenuItems, price.
#   'Butty' with columns MenuItems, price.
#   'Yurish' with columns MenuItems, price.
#   'DelD' with columns MenuItems, price.
#   'Subway' with columns MenuItems, price.
#   'Milan' with columns MenuItems, price.


# Connect to the MySQL server
db_connection = con.connect(
    host="localhost",
    user="root",
    password="123456",
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Check if the database "FoodDashDB" exists
cursor.execute("SHOW DATABASES LIKE 'FoodDashDB'")
database_exists = cursor.fetchone()

if not database_exists:
    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE FoodDashDB")
    print("Database created successfully.")

# Connect to the "FoodDashDB" database
db_connection = con.connect(
    host="localhost",
    user="root",
    password="123456",
    database="FoodDashDB",
)

# Create a new cursor after reconnecting
cursor = db_connection.cursor()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS CustomerData (
        uname VARCHAR(50),
        pass VARCHAR(50),
        name VARCHAR(50),
        mob VARCHAR(20),
        address VARCHAR(100),
        PRIMARY KEY (uname)
    )
""")

# Sample table creation for 'Evergreen'.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Evergreen (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")
# Sample table creation for 'Butty'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Butty (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")
# Sample table creation for 'Yurish'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Yurish (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")
# Sample table creation for 'DelD'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS DelD (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")
# Sample table creation for 'Subway'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subway (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")
# Sample table creation for 'Milan'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Milan (
        MenuItems VARCHAR(50),
        price DECIMAL(10, 2),
        PRIMARY KEY (MenuItems)
    )
""")

# Check if the Tables are empty before inserting values
cursor.execute("SELECT COUNT(*) FROM Evergreen")
if cursor.fetchone()[0] == 0:
    # Insert values into 'Evergreen' table
    cursor.execute("""
        INSERT INTO Evergreen (MenuItems, price)
        VALUES
        ('Fried Rice', 10.99),
        ('Roll', 8.49),
        ('Drink', 12.99)
    """)

# Check if the 'Butty' table is empty before inserting values
cursor.execute("SELECT COUNT(*) FROM Butty")
if cursor.fetchone()[0] == 0:
    # Insert values into 'Butty' table
    cursor.execute("""
        INSERT INTO Butty (MenuItems, price)
        VALUES
        ('Fried Rice', 7.99),
        ('Roll', 9.99),
        ('Drink', 6.49)
    """)

# Check if the 'Yurish' table is empty before inserting values
cursor.execute("SELECT COUNT(*) FROM Yurish")
if cursor.fetchone()[0] == 0:
    # Insert values into 'Yurish' table
    cursor.execute("""
        INSERT INTO Yurish (MenuItems, price)
        VALUES
        ('Fresh Lime', 15.99),
        ('Cold Drink', 11.49),
        ('Milk Shake', 18.99)
    """)

# Check if the 'DelD' table is empty before inserting values
cursor.execute("SELECT COUNT(*) FROM DelD")
if cursor.fetchone()[0] == 0:
    # Insert values into 'DelD' table
    cursor.execute("""
        INSERT INTO DelD (MenuItems, price)
        VALUES
        ('Fries Rice', 14.99),
        ('Rolls', 10.49),
        ('Biryani', 16.99)
    """)

# Check if the 'Subway' table is empty before inserting values
cursor.execute("SELECT COUNT(*) FROM Subway")
if cursor.fetchone()[0] == 0:
    # Insert values into 'Subway' table
    cursor.execute("""
        INSERT INTO Subway (MenuItems, price)
        VALUES
        ('12 Inch Sub', 6.99),
        ('6 Inch Sub', 8.99),
        ('Drink', 7.49)
    """)

# Check if the 'Milan' table is empty before inserting values
cursor.execute("SELECT COUNT(*) FROM Milan")
if cursor.fetchone()[0] == 0:
    # Insert values into 'Milan' table
    cursor.execute("""
        INSERT INTO Milan (MenuItems, price)
        VALUES
        ('Biryani', 13.99),
        ('Noodles', 9.49),
        ('Drink', 11.99)
    """)

# Commit the changes and close the cursor and connection
db_connection.commit()
cursor.close()
db_connection.close()



#MAIN PROGRAM
window = Tk()

window.geometry("800x500+300+200")
window.title("FoodDash")
window.config(background="#FFFFFF")

icon = PhotoImage(file="FoodDash_Icon.png")
window.iconphoto(True, icon)

namelogo = Image.open("FoodDash_LogoWithName.png")
logo = namelogo.resize((200, 200))
logo1 = ImageTk.PhotoImage(logo)

img1 = Label(window, image=logo1, bg="#FFFFFF")
img1.place(x=300, y=20)

# Keep a reference to the logo image
window.logo1 = logo1

def newUser():
    newUserLogIn()

newUserB = Button(window,
                  text="New User",
                  font=("Arial", 15, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404",
                  width=20,
                  command=newUser)
newUserB.place(x=280, y=260)

def existingUser():
    existingUserLogIn()

exUserB = Button(window,
                  text="Existing User",
                  font=("Arial", 15, "bold"),
                  fg="#FFFFFF",
                  bg="#FF5404",
                  width=20,
                  command=existingUser)
exUserB.place(x=280, y=320)

window.mainloop()
