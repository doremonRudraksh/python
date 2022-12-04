from tkinter import *
from tkinter import messagebox

from pyparsing import White

root= Tk()
root.title("Error handling")
root.geometry("600x400 ")
input_box = Entry(root)
input_box.pack()

def add():
    number=11
    get_number = input_box.get()

    try:
        print(number + get_number) 

    except:
        messagebox.showinfo("error", "CANNOT ADD TWO DIFFERENT DATA TYPES , TRYING TO ADD STRING AND INTEJER ")
btn= Button(root, text="Addition", bg="blue", fg="White", command=add)
btn.place(relx=0.5, rely=0.2,anchor=CENTER )
root.mainloop()