
from tkinter import *
from PIL import ImageTk, Image
import random 
root = Tk()

root.title("Endless Pokemon Game")
root.geometry("620x460")

root.configure(background = "orange")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
bulbasour= ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
lyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglipuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meoth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))

player_1 = Label(root, text="Player 1", bg="royal blue", fg="white")
player_1.place(relx=0.1, rely=0.3, anchor=CENTER)

player_2 = Label(root, text="Player 2", bg="red", fg="white")
player_2.place(relx=0.9, rely=0.3, anchor=CENTER)

player_score1 = Label(root, text="Player 1 score ", bg="royal blue", fg="white")
player_score1.place(relx=0.1, rely=0.4, anchor=CENTER)

player_score2 = Label(root, text="Player 2 score ", bg="red", fg="white")
player_score2.place(relx=0.9, rely=0.4, anchor=CENTER)


random_label = Label(root, bg = "white", fg = "orange")
random_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = [abra, bulbasour, charmender, lyvasour , jigglipuff, kadabra, meoth, nidoking, paras, persion, pikachu, ratata,]
power_list = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]
 
player_1_score = 0
def player1():
    global player_1_score
    random_no = random.randint(0, 11)
    random_pokemon = pokemon_list[random_no]
    random_label["image"] = random_pokemon
    
    random_power = power_list[random_no]
    player_1_score = player_1_score + random_power
    player_score1["text"] = str(player_1_score)

player1_btn=  Button(root, image=button, command=player1)
player1_btn.place(relx= 0.1, rely=0.6, anchor= CENTER)

player_2_score = 0
def player2():
    global player_2_score 
    random1 =  random.randint(0,11)
    random_pokemon1 = pokemon_list[random1]
    random_label["image"] = random_pokemon1
    
    random_power2 = power_list[random1]
    player_2_score = player_2_score + random_power2
    player_score2["text"] = str(player_2_score)

player2_btn=  Button(root, image=button, command=player2)
player2_btn.place(relx= 0.9, rely=0.6, anchor= CENTER)

   


root.mainloop()