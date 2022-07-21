from tkinter import *
from PIL import ImageTk, Image
import random 

root= Tk()

root.title("Endless dice game ")
root.geometry("600x400")

root.configure(background="yellow")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))



player1 = Label(root, text="Player 1 ", bg="royal blue", fg="white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2 ", bg="royal blue", fg="white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player_1_score = Label(root, text="", bg="royal blue", fg="white")
player_1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score = Label(root, text="", bg="royal blue", fg="white")
player_2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

random_dice= Label(root, text="", bg="orange", fg="white")
random_dice.place(relx=0.5, rely=0.6, anchor=CENTER)

player1_score = 0
player2_score = 0

def player1():
    global player1_score
    random_1= random.randint(1,6)
    random_dice["text"]= "PLayer 1 dice no. " + str(random_1)
    player1_score = player1_score+random_1
    player_1_score["text"] = " Player 1 score " + str(player1_score)

btn= Button(root, image= img, command=player1 )
btn.place(relx=0.1, rely=0.6, anchor=CENTER)


def player2():
    global player2_score
    random1= random.randint(1,6)
    random_dice["text"]= "player 2 dice no. " + str(random1)
    player2_score= player2_score+random1
    player_2_score["text"]= "player 2 score " +  str(player2_score)

btn1= Button(root, image= img, command=player2 )
btn1.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()