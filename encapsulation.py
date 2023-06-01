from tkinter import *

root=Tk()
root.geometry("800x600")
root.title("encapsulation")

class Fruit():

    def __init__(self, fruit, quantity):
        self.fruit_juice = fruit
        self.quantity = int(quantity)
        self.__cost = 250

    def __calculate(self):
        total_cost = self.quantity*self.__cost
        if (self.fruit_juice == "apple"):
            calorie = self.quantity*52

        if (self.fruit_juice == "mango"):
            calorie = self.quantity*60

        if (self.fruit_juice == "orange"):
            calorie = self.quantity*47
       
        print("x"+ str(self.quantity) + " = " + str(calorie) + "calories")

    def get_cost(self):
        self.__calculate()   

def order_juice():
    fruit = "apple"
    quantity = 250
    obj1 = Fruit(fruit, quantity)
    obj1.get_cost()

btn1 = Button(root, text="Order juice", fg="blue", command=order_juice)
btn1.pack()

root.mainloop()
            
        
