from tkinter import *
from PIL import Image, ImageTk
import mysql.connector as con
from RestaurantOptions import *

def newUserDetails(username):
    win4 = Toplevel()

    win4.geometry("800x500+300+200")
    win4.title("FoodDash")
    win4.config(background="#FFFFFF")

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win4, image=logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win4.iconphoto(True, icon)

    # Keep a reference to the logo image
    win4.logo1 = logo1

    title = Label(win4,
                  text="Personal Details",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=240, y=30)

    name1 = Label(win4,
                  text="Name                  :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    name1.place(x=120, y=180)
    ntxt1 = Entry(win4,
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF")
    ntxt1.place(x=380, y=180) 
    mobNo1 = Label(win4,
                  text="Mobile Number      :  ",
                  font=("Arial", 19, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    mobNo1.place(x=120, y=230)
    mobNotxt1 = Entry(win4,
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF")
    mobNotxt1.place(x=380, y=230)   
    adrs1 = Label(win4,
                  text="Address              :  ",
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    adrs1.place(x=120, y=280)    
    adrstxt1 = Text(win4,
                  font=("Arial", 20, "bold"),
                  bg="#FFFFFF",
                  height=3,
                  width=20)
    adrstxt1.place(x=380, y=280)

    def SaveAndGoToRestaurantsPg(ntxt, mobNotxt, adrstxt, window, uname):
        # Retrieve values from the Entry and Text widgets
        name = ntxt.get()
        mobile_number = mobNotxt.get()
        address = adrstxt.get("1.0", "end-1c")  # Get text from the Text widget

        # Connect to the MySQL database
        db_connection = con.connect(
            host="localhost",
            user="root",
            password="123456",
            database="FoodDashDB",
        )

        # Create a cursor object to execute SQL queries
        cursor = db_connection.cursor()

        # Update values in 'CustomerData' table
        cursor.execute("""
            UPDATE CustomerData
            SET name = %s, mob = %s, address = %s
            WHERE uname = %s
        """, (name, mobile_number, address, uname))

        # Commit the changes and close the cursor and connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

        # Call the function to open the next page (RestaurantOptions.py)
        restaurantOptions()

        # Close the current window
        window.destroy()

    LogInB = Button(win4,
                    text="Save",
                    font=("Arial",18, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    padx=50,
                    pady=0,
                    command=lambda: SaveAndGoToRestaurantsPg(ntxt1, mobNotxt1, adrstxt1, win4, username))
    LogInB.place(x=310,y=400)
