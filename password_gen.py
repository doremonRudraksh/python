from tkinter import *
import random

root=Tk()
root.title("Password generator")
root.geometry("400x400")

input_1 = Entry(root)
guessed_passwaord= Label(root)
generated_password= Label(root)

array3d = [[["1", "2", "3", "4", "5", "6" , "7", "8", "9", "10", "@", "#", "$", "%"], ["head", "tails", "king", "queen", "pass", "food", "play"], ["a", "b", "c", "d", "e", "f", "g", "h", "I", "J", "K", "L", "M", "N", "P", "Q"] ]]
print(array3d[0][2][3])

def new_password():
    random_number1 = random.randint(0,13)
    random_number2 = random.randint(0,6)
    random_number3 = random.randint(0,15)

    letter1= array3d[0][0][random_number1]
    letter2= array3d[0][1][random_number2]
    letter3= array3d[0][2][random_number3]

    guessed_passwaord["text"]= "Guessed password : " + input_1.get() 
    generated_password["text"]= "Generated password : " + letter1 + letter2 +  letter3

btn = Button(root, text = "New Password", command = new_password, fg="black")
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

input_1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
guessed_passwaord.place(relx = 0.5, rely = 0.4, anchor = CENTER)
generated_password.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()
