from tkinter import *
import random

root = Tk()
root.title("Sales Application")
root.geometry("900x400")
root.configure(background = "yellow")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

month_label = Label(root)
month_label["text"] = "Months : " + str(months)
month_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

profit_label = Label(root)
profit_label["text"]= "Profit : " + str(profits)
profit_label.place(relx=0.5, rely=0.3, anchor=CENTER)

max_profit = Label(root)
max_profit.place(relx=0.5, rely=0.5, anchor=CENTER)

min_profit = Label(root)
min_profit.place(relx=0.5, rely=0.7, anchor=CENTER)

def max1():
    max_profit1 = max(profits)
    max_profit_index = profits.index(max_profit1)
    max_profit_month = months[max_profit_index]
    max_profit["text"] = "Maximum profit of " + str(max_profit1) + " was given in the month of " + str(max_profit_month) + " ."

def min1():
    min_profit1 = min(profits)
    min_profit_index = profits.index(min_profit1)
    min_profit_month = months[min_profit_index]
    min_profit["text"] = "Minimum profit of " + str(min_profit1) + " was given in the month of " + str(min_profit_month) + " ."

btn= Button(root, text="Show max profitable month", command=max1,  bg="blue", fg="white")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

btn2 = Button(root, text="Show min profitable month", command=min1, bg="blue", fg="white")
btn2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()