from cProfile import label
from cgitb import text
from tkinter import *
import random

root = Tk()
root.title("Encryption with ascii code")
root.geometry("400x400")
root.configure(background= "yellow")

input_user = Entry(root)
input_user.place(relx=0.5, rely = 0.5, anchor=CENTER)

name_in_ascii = Label(root, text="name in ascii: ", bg="light cyan", fg="black" )
encrypted_name = Label(root, text="encrypted name ", bg="light cyan", fg="black") 

def asciiConverter():
    input_word= str(input_user.get())

    for r in input_word:
        name_in_ascii["text"]+=str(ord(r))+ " "
        ascii= int(ord(r))
        encrypted= ascii-1
        encrypted_name["text"]+=str(chr(encrypted)) + " "

btn=Button(root, text="Display the ascii and encrypted value", command=asciiConverter, bg="royalblue",fg="white")  
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

name_in_ascii.place(relx=0.5, rely=0.6, anchor=CENTER)
encrypted_name.place(relx=0.5, rely=0.7, anchor=CENTER)




root.mainloop()
