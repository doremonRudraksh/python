from tkinter import *
import random

root=Tk()
root.title("Password generator")
root.geometry("400x400")

label1= Label(root)

array3d = [[["1", "2", "3", "4", "5", "6"], ["head", "tails"], ["a", "b", "c", "d", "e", "f", "g", "h"] ]]
print(array3d[0][2][3])

def newpassword():
    random1 = random.randint(0,5)
    random2 = random.randint(0,1)
    random3 = random.randint(0,7)

    letter1 = str(array3d[0][0][random1])
    letter2 = (array3d[0][1][random2])
    letter3= (array3d[0][2][random3])
    label1["text"]= letter1+letter2+letter3

btn= Button(root, text="Password generator", command=newpassword, fg="black")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label1.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()

