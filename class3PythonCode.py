from cProfile import label
from tkinter import *

root = Tk()

root.title("Ascii")
root.geometry("400x400")
root.configure(background= "snow")



enter_word = Entry(root)
enter_word.place(relx=0.5, rely = 0.5, anchor=CENTER)

label = Label(root,text="name in Ascii: ", bg="light yellow", fg="black")



def asciiConverter():
    input_word = enter_word.get()

    for r in input_word:
        Label2["text"]+=str(chr(r)) + " "

btn=Button(root, text="Show name in ascii", command=asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
label.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()


        




