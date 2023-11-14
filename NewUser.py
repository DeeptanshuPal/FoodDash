from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as con
from UserDetailsPg import *

def newUserLogIn():
    win2 = Toplevel()

    win2.geometry("800x500+300+200")
    win2.title("FoodDash")
    win2.config(background="#FFFFFF")

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win2, image = logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win2.iconphoto(True, icon)

    # Keep a reference to the logo image
    win2.logo1 = logo1

    title = Label(win2,
                  text="Sign Up",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=320, y=30)

    uname1 = Label(win2,
                  text="Username  :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    uname1.place(x=150, y=180)
    untxt1 = Entry(win2,
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF")
    untxt1.place(x=350, y=180)    
    passwd1 = Label(win2,
                  text="Password  :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    passwd1.place(x=150, y=230)    
    pwdtxt1 = Entry(win2,
                  font=("Arial", 20, "bold"),
                  show=str('*'),
                  bg="#FFFFFF")
    pwdtxt1.place(x=350, y=230)

    def logIn():
        # Retrieve values from the Entry widgets
        username = untxt1.get()
        password = pwdtxt1.get()

        # Connect to the MySQL database
        db_connection = con.connect(
            host="localhost",
            user="root",
            password="123456",
            database="FoodDashDB",
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Check if the entered username already exists in 'CustomerData' table
        cursor.execute("""
            SELECT * FROM CustomerData
            WHERE uname = %s
        """, (username,))

        result = cursor.fetchone()

        if result:
            # If a matching record is found, display an error message
            invalidL = Label(win2,
                  text="* Username already exists",
                  font=("Arial", 15),
                  bg="#FFFFFF",
                  fg="red")
            invalidL.place(x=350, y=270)
        else:
            # If the username doesn't exist, proceed to sign up
            # Insert values into 'CustomerData' table
            cursor.execute("""
                INSERT INTO CustomerData (uname, pass)
                VALUES (%s, %s)
            """, (username, password))

            # Commit the changes and close the cursor and connection
            db_connection.commit()
            cursor.close()
            db_connection.close()

            # Call the function to open the next page (UserDetailsPg.py)
            newUserDetails(untxt1.get())

            # Close the current window
            win2.destroy()

    LogInB = Button(win2,
                    text="Sign Up",
                    font=("Arial",15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    width=20,
                    command=logIn)
    LogInB.place(x=280,y=320)
