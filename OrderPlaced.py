from tkinter import *
from PIL import Image, ImageTk

def orderPlaced():
    win7 = Toplevel()

    win7.geometry("800x500+300+200")
    win7.title("FoodDash")
    win7.config(background="#FFFFFF")

    #displaying the gif
    def update_gif_frame(frame_idx=0):
        GIFlabel.configure(image=frame_list[frame_idx])
        win7.after(100, update_gif_frame, (frame_idx + 1) % len(frame_list))
    gif = "OrderPlaced.gif"
    frame_list = [PhotoImage(file=gif, format=f"gif -index {i}") for i in range(33)]
    GIFlabel = Label(win7,
                     bg="#FFFFFF")
    GIFlabel.place(x=0,y=-150)
    update_gif_frame()

    ##displaying logo
    namelogo = Image.open("FoodDash_LogoWithName.png")
    logo = namelogo.resize((100,100))
    logo1 = ImageTk.PhotoImage(logo)

    img1 = Label(win7, image = logo1, bg="#FFFFFF")
    img1.place(x=20, y=5)

    icon = PhotoImage(file="FoodDash_Icon.png")
    win7.iconphoto(True, icon)
    # Keep a reference to the logo image
    win7.logo1 = logo1

    title = Label(win7,
                  text = "Hurray!\nOrder Placed!\nYour Order is on the Way.............",
                  font=("Arial",20, "bold"),
                  bg="#FFFFFF",
                  fg="#5957b5")
    title.place(x=180,y=320)


    rider = Image.open("Rider.png")
    img2 = rider.resize((40,40))
    pic = ImageTk.PhotoImage(img2)
    # Keep a reference to the logo image
    win7.pic = pic

    riderImg1 = Label(win7, image = pic, bg="#FFFFFF")
    riderImg1.place(x=515, y=375)
    riderImg2 = Label(win7, image = pic, bg="#FFFFFF")
    riderImg2.place(x=559, y=375)
    riderImg3 = Label(win7, image = pic, bg="#FFFFFF")
    riderImg3.place(x=603, y=375)
