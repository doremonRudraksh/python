from tkinter import *
from PIL import ImageTk, Image

root= Tk()

root.title("Endless dice game ")
root.geometry("600x400")

root.configure(background="yellow")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1 = Label(root, text="Player 1 ", bg="royal blue", fg="white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2 ", bg="royal blue", fg="white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player1_score = Label(root, text="", bg="royal blue", fg="white")
player1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score = Label(root, text="", bg="royal blue", fg="white")
player2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

random1= Label(root, text="", bg="orange", fg="white")
random1.place(relx=0.5, rely=0.6)

root.mainloop()