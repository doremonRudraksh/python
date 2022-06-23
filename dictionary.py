from tkinter import *
import tkinter

root=Tk()
root.title("Dictionary")
root.geometry("400x400")

label_of_mutable= Label(root)
label_of_immutable= Label(root)
label_of_tkinter= Label(root)

dictionary= {
    "mutable" : "Values can be changed just like lists.",
    "immutable" : "Values cannot be changed just like tupples.",
    "Tkinter" : "It is a python gui library"
}

def mute():
    label_of_mutable["text"]= dictionary["mutable"]

def immute():
    label_of_immutable["text"]= dictionary["immutable"]

def tk():
    label_of_tkinter["text"]= dictionary["Tkinter"]


btn1= Button(root, text="Meaning of Mutable", command=mute)
btn1.place(relx=0.5, rely=0.2, anchor=CENTER)

label_of_mutable.place(relx=0.5, rely=0.3, anchor=CENTER)

btn2= Button(root, text="Meaning of Immutable", command=immute)
btn2.place(relx=0.5, rely=0.4, anchor=CENTER)

label_of_immutable.place(relx=0.5, rely=0.5, anchor=CENTER)

btn3= Button(root, text="Meaning of Tkinter", command=tk)
btn3.place(relx=0.5, rely=0.6, anchor=CENTER)

label_of_tkinter.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()