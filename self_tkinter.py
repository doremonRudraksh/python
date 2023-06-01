from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("classes")
root.geometry("1000x600")

class CreateElement:
    def __init__(self):
        print("this is a element class")

    def create_new_element(self):
        label1 = Label(root, text="this label has been created using the create element class", fg="red")
        label1.pack()     
        btn1 = Button(root, text="Click", bg="blue", fg="white", command=self.message)
        btn1.pack(padx=20, pady=10)

    def message(self):
        messagebox.showinfo("showinfo", "you have pressed the button created by the create element class.")

obj_create = CreateElement()
btn2 = Button(root, text="click to create label and button", command=obj_create.create_new_element)
btn2.pack(padx=20, pady=10)

root.mainloop()
