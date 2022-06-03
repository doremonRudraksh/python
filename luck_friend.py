from cgitb import text
from tkinter import*
import random

root= Tk()
root.title("luck freind wheel")

root.geometry("400x400")
root.configure(background="royalblue")

friend_name = Entry(root)
friend_name.place(relx=0.5, rely=0.2, anchor=CENTER)

friend_list = Label(root)
random_number_label = Label(root)
lucky_friend_label = Label(root)

friend=[]

def add_friend():
    get_friend = friend_name.get()
    friend.append(get_friend)
    friend_list["text"]= "your friend list : " + str(friend)

def lucky_friend():
    length = len(friend)
    random_number = random.randint(0, length-1)
    random_number_label["text"]= str(random_number)
    generator_random_number = friend[random_number]
    lucky_friend_label["text"] = "your lucky friend is" + str(generator_random_number)

btn= Button(root, text="Add to the friend list", command=add_friend, bg="blue", fg="white")
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

friend_list.place(relx=0.5, rely=0.4, anchor=CENTER)

btn1 = Button(root, text="Who is your luck friend", command=lucky_friend, bg="green", fg="white")

random_number_label.place(relx=0.5, rely=0.5, anchor=CENTER)
lucky_friend_label.place(relx=0.5, rely=0.7, anchor= CENTER)



    

root.mainloop()

