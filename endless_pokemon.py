
from tkinter import *
from PIL import ImageTk, Image
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

root.mainloop()