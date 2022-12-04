from cgitb import html
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import webbrowser




root = Tk()
# root.geometry("500x250")
root.minsize(650,650)
root.maxsize(650,650)
open_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label_file_name = Label(root, text="File Name", fg="Blue")
label_file_name.place(relx=0.40, rely= 0.05, anchor=CENTER)

input_file =Entry(root)
input_file.place(relx=0.57, rely=0.05, anchor=CENTER)

my_text = Text(root, height = 33, width = 74, bg = "gray", fg = "Blue")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)


open_button = Button(root, image = open_img, text = "Open File")
open_button.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_button = Button(root, image = save_img, text= "Save file")
save_button.place(relx = 0.15, rely = 0.05, anchor = CENTER)


run_button = Button(root, image= exit_img, text= "Exit file")
run_button.place(relx = 0.23, rely = 0.05, anchor = CENTER)

name= ""

def open_file():
    global name
    my_text.delete(1.0, END)
    input_file.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Open Html File", filetypes = (("Html Files", "*.html"), ))                                                                                  
    print(html_file)
    name= os.path.basename(html_file)
    formatted_name = name.split(".")[0]
    input_file.insert(END, formatted_name)
    root.title(formatted_name)
    html_file= open(name, "r")
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    html_file.close()

def save():
    input_name = input_file.get()
    file = open(input_name + ".html" +"w")
    data = my_text.get(1.0, END)
    print(data)
    file.write(data)
    input_file.delete()
    input_file.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")

def run():
    webbrowser.open(name)

open_button = Button(root, image = open_img, text = "Open File", command = open_file)
open_button.place(relx = 0.05, rely = 0.05, anchor = CENTER)

save_button = Button(root, image = save_img, text = "Save File", command = save)
save_button.place(relx = 0.15, rely = 0.05, anchor = CENTER)

run_button = Button(root, image = exit_img, text = "Run File", command=run)
run_button.place(relx = 0.23, rely = 0.05, anchor = CENTER)

    


root.mainloop()
