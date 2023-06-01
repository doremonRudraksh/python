class Parent():
    def __init__(self):
        print("this is parent class")

    def menu(dish):
        if(dish == "burger"):
            print("You can add the following toppings.")
            print("More cheese | Jalepeno")

        elif(dish == "iced americano"):
            print("You can add the following toppings.")
            print("chocolate | caramel")

        else:
            print("Invalid dish")

    def final_amount(dish, add_ons):
        if(dish == "burger" and add_ons == "cheese"):
            print("You have to pay 250 usd.")

        elif(dish == "burger" and add_ons == "Jalapeno"):
            print("You have to pay 350 usd.")

        elif(dish == "iced americano" and add_ons == "Caramel"):
            print("You have to pay 450 usd.")

        elif(dish == "iced americano" and add_ons == "chocolate"):
            print("You have to pay 250 usd.")

class Child_1(Parent):

    def __init__(self, dish):
        self.dish = dish

    def get_menu(self):
        Parent.menu(self.dish)

class Child_2(Parent):

    def __init__(self, dish, addons):
        self.dish = dish
        self.addons = addons

    def get_final_amount(self):
        Parent.final_amount(self.dish, self.addons)

child1_obj = Child_1("burger")
child1_obj.get_menu()

child2_obj = Child_2("iced americano","Caramel")
child2_obj.get_final_amount()



        
        