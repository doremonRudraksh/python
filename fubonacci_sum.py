from tkinter import *

root = Tk()

root.title("fibonacci")
root.geometry("400x400")
root.configure(background= "snow")

label_series = Label(root, text="Fibonacci sum")
input1= Entry(root)
fc = Label(root)

def fibonacci():
    num1= int(input1.get())
    sum2= 0
    first_num = 0
    second_num = 1
    sum1 = 0
    counter = 1
    while(counter <= num1):
        counter+=1
        first_num=second_num
        second_num=sum1
        sum1=first_num+second_num
        sum2 = sum2+sum1
        label_series["text"]+= str(sum1) + " "
        fc["text"] = "Fibonacci Sum : " + str(sum2)

btn= Button(root, text="Show fibonacci series", command=fibonacci, bg="cyan")
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
input1.pack()
input1.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.pack()
label_series.pack()
fc.pack()





        







root.mainloop()


        




