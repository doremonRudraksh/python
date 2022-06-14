from array import array
from cProfile import label
from logging import root
from tkinter import *
root= Tk()
root.title("Multidimensional list")
root.geometry("500x500")
label1 = Label(root)

array1d = ["john", "James", "thomsan"]
print( array1d[0] )

array2d = [["john", "A"], ["James","B"], ["thomsan", "C"]]
print( array2d[0][1] )

array3d = [[["John", "A+", "Excellent"], ["James", "A", "very good"], ["Thomsan", "B", "Good"]]]
print(array3d[0][0][2])

def report():
    label1["text"]= array3d[0][0][0] + " has got the grade " + array3d[0][0][1] +"and he is doing " + array3d[0][0][2]

btn= Button(root, text="Report", command=report, bg="blue", fg="white")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label1.place(relx=0.5, rely=0.6, anchor=CENTER)


root.mainloop()