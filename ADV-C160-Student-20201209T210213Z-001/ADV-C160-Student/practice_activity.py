from tkinter import *
from tkinter import filedialog 
from PIL import ImageTk, Image
import os


root = Tk()
# root.geometry("500x250")
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))


label_file_name = Label(root, text=" File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)


# Define clearInputFeild() function


# Define clearTextarea() function


# Define addData() function



open_button=Button(root,image=open_img, text="Open file", command=)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root image=save_img , text="Save file", command=)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
exit_button=Button(root image=exit_img, text="Exit file", command=)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)

root.mainloop()

