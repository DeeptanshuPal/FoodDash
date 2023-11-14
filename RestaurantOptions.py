from tkinter import *
from PIL import Image, ImageTk
from Menu import *

def restaurantOptions():
    win3 = Toplevel()

    win3.geometry("800x500+300+200")
    win3.title("FoodDash")
    win3.config(background="#FFFFFF")

    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win3, image = logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win3.iconphoto(True, icon)

    # Keep a reference to the logo image
    win3.logo1 = logo1

    title = Label(win3,
                  text="Our Restaurants",
                  font=("Elephant", 30, "bold"),
                  bg="#FFFFFF",
                  fg="#FF5404")
    title.place(x=250, y=30)


    #Restaurant Title Images
    nameR1 = Image.open(".\Restaurant Logos\EverGreenLogo.png")
    R1 = nameR1.resize((200,50))
    r1 = ImageTk.PhotoImage(R1)
    win3.r1 = r1

    nameR2 = Image.open(".\Restaurant Logos\SubWayLogo.png")
    R2 = nameR2.resize((200,50))
    r2 = ImageTk.PhotoImage(R2)
    win3.r2 = r2

    nameR3 = Image.open(".\Restaurant Logos\ButtyLogo.png")
    R3 = nameR3.resize((200,50))
    r3 = ImageTk.PhotoImage(R3)
    win3.r3 = r3

    nameR4 = Image.open(".\Restaurant Logos\YurishLogo.png")
    R4 = nameR4.resize((200,50))
    r4 = ImageTk.PhotoImage(R4)
    win3.r4 = r4

    nameR5 = Image.open(".\Restaurant Logos\DelDLogo.png")
    R5 = nameR5.resize((200,50))
    r5 = ImageTk.PhotoImage(R5)
    win3.r5 = r5

    nameR6 = Image.open(".\Restaurant Logos\MilanLogo.png")
    R6 = nameR6.resize((200,50))
    r6 = ImageTk.PhotoImage(R6)
    win3.r6 = r6


    #Restaurant image Buttons
    
    #func
    def menu(restaurant_name):
        win3.withdraw()  # Hide the current window
        getMenu(restaurant_name)

    res1 = Button(win3,
                image = r1,
                command=lambda: menu("evergreen"))
    res1.place(x=50, y=180)

    res2 = Button(win3,
                image = r2,
                command=lambda: menu("subway"))
    res2.place(x=300, y=180)

    res3 = Button(win3,
                image = r3,
                command=lambda: menu("butty"))
    res3.place(x=550, y=180)

    res4 = Button(win3,
                image = r4,
                command=lambda: menu("yurish"))
    res4.place(x=50, y=280)

    res5 = Button(win3,
                image = r5,
                command=lambda: menu("deld"))
    res5.place(x=300, y=280)

    res6 = Button(win3,
                image = r6,
                command=lambda: menu("milan"))
    res6.place(x=550, y=280)
