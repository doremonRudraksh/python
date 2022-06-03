from cgitb import text
from tkinter import*
import random

root= Tk()
root.title("random word generator")

root.geometry("400x400")
root.configure(background="royal blue")

label1 = Label(root, text="", fg="black")

def generate_word():
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i" , "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", ""]
    random_number1 = random.randint(0,25)
    random_number2 = random.randint(0,25)
    random_number3 = random.randint(0,25)
    random_number4 = random.randint(0,25)
    random_number5 = random.randint(0,25)

    random_alpha1 = alpha_list[random_number1]
    random_alpha2 = alpha_list[random_number2]
    random_alpha3 = alpha_list[random_number3]
    random_alpha4 = alpha_list[random_number4]
    random_alpha5 = alpha_list[random_number5]

    label1["text"]= random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5



btn = Button(root, text="Generate random word",  command=generate_word, bg="white", fg="red")
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()
    


