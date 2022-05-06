from tkinter import *
import random

root = Tk()
root.geometry("300x300+500+100")
root.title("Dice rolling")
root.config(bg="#ffffff")

colors = [
        "red",
        "blue",
        "green",
        "purple",
        "yellow",
        "orange"
    ]
label = Label(root, font="exo 140 bold", text="", bg="#ffffff", fg=f"{random.choice(colors)}")

def rollDiece():
    dice = [
        #dice sticker
        "\u2680", #show 1
        "\u2681", #show 2
        "\u2682", #show 3
        "\u2683", #show 4
        "\u2684", #show 5
        "\u2685" #show 6
    ]
    label.config(text=f"{random.choice(dice)}")
    label.pack()

button = Button(root, font="exo 15 bold", text="Dice roll", bg="#000040", fg="#ffffff", bd=0, command=rollDiece, cursor="hand2")
button.place(x=0, y=270, height=30, width=300)

root.mainloop()
