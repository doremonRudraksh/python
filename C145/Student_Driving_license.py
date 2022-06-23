# Basic tkinter template

from cgitb import text
from email.headerregistry import Address
from lib2to3.pytree import LeafPattern
from tkinter import *
root = Tk()

root.title("Driving License")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id=Label(root)
label_name=Label(root)
label_dob=Label(root)
label_pin=Label(root)
label_address=Label(root)
label_vehicle_type=Label(root)


# Define the function
def licence():
    id_value=8970435210
    print(type(id_value))
    name="Winnie The Pooh"
    print(type(name))
    dob="21 august 1921"
    print(type(dob))
    pin=451478
    print(type(pin))
    address="Disney Land , Honk Kong "
    print(type(address))
    vehicle_type= ["two", "four"]
    print(type(vehicle_type))

    label_id["text"]= id_value
    label_name["text"]= name
    label_dob["text"]= dob
    label_pin["text"]= pin
    label_address["text"]= address
    label_vehicle_type["text"]= vehicle_type

    
# Create a button
button1= Button(root, text="show my driving license ", command=licence)
button1.pack()

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()