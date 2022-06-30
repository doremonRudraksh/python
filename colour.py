from tkinter import *
import random

root= Tk()
root.title("Dictionarie")
root.geometry("400x400")

dictionarie = {"color" :  [
    "maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"

]}

def bg_1colour():
    random_colour = random.randint(0,7)
    print(dictionarie["color"][random_colour])
    root.configure(background = dictionarie["color"][random_colour])

btn= Button(root, text="Click me ", command=bg_1colour,)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
