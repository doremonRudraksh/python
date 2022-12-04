from email.mime import image
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from PIL import ImageTk, Image
import os
from tkinter import ttk

root= Tk()
root.geometry("500x500")
root.configure(background="black")

label_img= Label(root, bg="white", highlightthickness=5)
label_img.place(relx=0.5, rely=0.5, anchor=CENTER)

directs = ["Left", "Right", "Up", "Down"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = directs, textvariable = selectedval)

img_path = ""

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(title= "Open Image file", filetypes = [("Image Files", "*.jpg *.png *.gif *.jpeg *.jfif *.jpe")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    name = os.path.basename(img_path)
    formatted_name = name.split(".")[0]
    root.title(formatted_name)
    label_img["image"] = img
    img.close()

btn = Button(root, text="Open image", bg="grey", fg="white", font=("Century Schoolbook", 15, "bold"), padx=15, pady=10, relief=SOLID, command=open_image)
btn.place(relx=0.5, rely =0.1, anchor= CENTER)

def rotate_img():
    global img_path
    direct = selectedval.get()

    if direct == "Left":
        im= Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(270))
        print(img_path)
        label_img["image"] = img
        img.close()
        
    elif(direct == "Right"):
        im= Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(90))
        print(img_path)
        label_img["image"] = img
        img.close()

    elif(direct == "Up"):
        im= Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(180))
        print(img_path)
        label_img["image"] = img
        img.close()

    elif(direct == "Down"):
        im= Image.open(img_path)
        img = ImageTk.PhotoImage(im.rotate(0))
        print(img_path)
        label_img["image"] = img
        img.close()

dropdown.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
open_btn = Button(root, text = "Open Image", bg = "Blue", fg = "white", font = ("Vivaldi", 15, "bold", "italic"), padx = 15, pady = 10, relief = SOLID, command = open_image)
open_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

rotate_btn = Button(root, text = "Rotate Image", bg = "Blue", fg = "white", font = ("Vivaldi", 15, "bold", "italic"), padx = 15, pady = 10, relief = SOLID, command = rotate_img)
rotate_btn.place(relx = 0.5, rely = 0.9, anchor = CENTER)


root.mainloop()