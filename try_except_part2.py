from email import message
from tkinter import *
from tkinter import messagebox

root= Tk()
root.geometry("600x400")

list=["micky mouse", "elsa", "anna", "donald duck"]
shinchan_dict = {"name" : "shinchan", "name1" : "doremon", "name2" : "dexter",
                    "age" : "11",  "age1" : "3" , "age2" : "95"}

try:                 
    for r in range(0,3):
        print(list[r])
    
    print(shinchan_dict["uncle"])


    


except IndexError:
    messagebox.showinfo("error", "this index does not exist")

except KeyError:
    messagebox.showerror("error", "this  key does not exist")
    


