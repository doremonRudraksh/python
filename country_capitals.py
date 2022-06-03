from itertools import count
from tkinter import *
import random 


root= Tk()
root.title("Random Country and capital")

root.geometry("400x400")
root.configure(background="white")

country_name  = Entry(root)
country_name.place(relx=0.5, rely=0.2, anchor=CENTER)

captital_name = Entry(root)
captital_name.place(relx=0.5, rely=0.3, anchor=CENTER)

country_list = Label(root)
city_list = Label(root)
random_country = Label(root)
random_city = Label(root)

list1 = []
list2 = []

def input_data():
    country = country_name.get()
    list1.append(country)
    country_list["text"]= "Country name : " + str(list1)

    capital = captital_name.get()
    list2.append(capital)
    city_list["text"]= "City name : " +str(list2)

def random_number():
    length1= len(list1)
    random_number = random.randint(0, length1-1)
    index = list1[random_number]
    random_country["text"]= "Random country : " +str(index)

    length= len(list2)
    random_number1 = random.randint(0, length-1)
    index1 = list2[random_number1]
    random_city["text"]= "Random Capital : " +str(index1)

btn= Button(root,text="Display country and city name", command=input_data, bg="blue", fg="white")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

country_list.place(relx=0.5, rely=0.5, anchor=CENTER)
city_list.place(relx=0.5, rely=0.6, anchor=CENTER)

btn1 = Button(root, text="Display country and city name randomly", command=random_number, bg="blue", fg="white")
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)

random_country.place(relx=0.5, rely=0.8, anchor=CENTER)
random_city.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()






