import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import messagebox

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.config(background="yellow")
registration_window.title("Sign Up")

firebase = firebase.FirebaseApplication("https://dloginsystem-15f82-default-rtdb.firebaseio.com/",None)

login_username_entry = ""
login_password_entry = ""

def login(): 
    print("login function")
    global login_username_entry
    global login_password_entry

    username = login_username_entry.get()
    password = login_password_entry.get()

    encrypted_password = hashlib.md5(password.encode())
    hexdecimal_password = encrypted_password.hexdigest()
    get_password = firebase.get("/",username)
    print(hexdecimal_password)

    if get_password != NONE:
        if get_password != hexdecimal_password:
            messagebox.showinfo("Information", " successfully logged in")

        else:
            messagebox.showinfo("Information", " Please check your password")

    else:
        messagebox.showinfo("Information", "User Not Registered! \n Get Yourself Registered 1st To Login")

def register(): 
    print("register function")

    username = username_entry.get()
    password = password_entry.get()

    encrypyted_password = hashlib.md5(password.encode())
    hex_decimal = encrypyted_password.hexdigest()
    print(hex_decimal)
    firebase.get("/",username)

    messagebox.showinfo("Information", "Successfully Registered")
    
def login_window():
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.title("Login")
    login_window.config(background="red")

    registration_window.destroy()
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold', bg="red")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13',bg="red")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13',bg="red")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT,bg="yellow",fg="black")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', fg="Green",bg="black")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
username_label = Label(registration_window, text="Username : " , font = 'arial 13',fg="green",bg="black")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13',fg="green",bg="black")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10,fg="Green", bg="black")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT, fg="green",bg="black")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()

