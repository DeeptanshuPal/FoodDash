from tkinter import *
from PIL import Image, ImageTk
from OrderPlaced import *

def orderSummary():
    win6 = Toplevel()

    win6.geometry("800x500+300+200")
    win6.title("FoodDash")
    win6.config(background="#FFFFFF")

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win6, image = logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win6.iconphoto(True, icon)

    # Keep a reference to the logo image
    win6.logo1 = logo1

    title = Label(win6,
                  text="Order Summary",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=260, y=30)

    #fetch from database

    def placeOrder():
        orderPlaced()
        win6.destroy()
    LogInB = Button(win6,
                    text="Place Order",
                    font=("Arial",15, "bold"),
                    fg="#FFFFFF",
                    bg="#FF5404",
                    padx=50,
                    pady=0,
                    command=placeOrder)
    LogInB.place(x=310,y=370)