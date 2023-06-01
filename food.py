from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title("FOOD APP")
root.geometry("900x500")

burger = ImageTk.PhotoImage(Image.open("burger1.png"))
burger_label = Label(root)
burger_label["image"] = burger
burger_label.place(relx = 0.7, rely=0.5 , anchor =CENTER)

heading = Label(root, text="RDONALDS", font = ("times",40,"bold"),fg="orange")
heading.place(relx=0.12, rely=0.1, anchor=CENTER)


select_dish = Label(root, text="Select dish", font = ("times",15))
select_dish.place(relx=0.06, rely=0.2, anchor=CENTER)


select_addons = Label(root, text="Select addons", font = ("times",15))
select_addons.place(relx=0.08, rely=0.5, anchor=CENTER)


dish_amount = Label(root, font = ("times",15, "bold"))
dish_amount.place(relx=0.2, rely=0.75, anchor=CENTER)

dish = ["burger", "iced americano"]
dish_dropdown = ttk.Combobox(root, state = "readonly", values = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

toppings = [""]
addons_dropdown = ttk.Combobox(root, state = "readonly", values = toppings)
addons_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

class Parent:
    def __init__(self):
        print("this is a parent class")

    def menu(dish):
        if(dish == "burger"):
            toppings  = ["cheese", "jalapeno"]
            addons_dropdown["values"] = toppings

        elif(dish == "iced americano"):
            toppings = ["chocolate", "caramel"]
            addons_dropdown["values"] = toppings
        
    def final_amount(dish, addons):
        if dish == "burger" and addons == "cheese":
            dish_amount["text"] = "You need to pay 250 USD"

        
        elif dish == "burger" and addons == "jalepeno":
            dish_amount["text"] = "You need to pay 350 USD"

        
        elif dish == "iced americano" and addons == "chocolate":
            dish_amount["text"] = "You need to pay 350 USD"

        
        elif dish == "iced americano" and addons == "caramel":
            dish_amount["text"] = "You need to pay 450 USD"


class child_1(Parent):
    def __init__(self):
        print("hi")

    def get_menu(self):
        new_dish = dish_dropdown.get()
        Parent.menu(new_dish)

class child_2(Parent):
    def __init__(self):
        print("hi")

    def get_final_amount(self):
        new_dish = dish_dropdown.get()
        addons = addons_dropdown.get()
        Parent.final_amount(new_dish, addons)

obj1 = child_1()
obj2 = child_2()

button = Button(root, text="check addons", command=obj1.get_menu, bg="blue", fg="white")
button.place(relx = 0.06, rely=0.3, anchor = CENTER)


button_2 = Button(root, text="check amount", command=obj2.get_final_amount, bg="blue", fg="white")
button_2.place(relx = 0.04, rely=0.6, anchor = CENTER)

root.mainloop()