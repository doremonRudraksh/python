from tkinter import *
root = Tk()

root.title("Private Variable Login Page")
root.geometry("600x600")

name_lbl = Label(root, text="Name")
name_lbl.place(relx=0.4, rely=0.1, anchor=CENTER)

name_entry = Entry(root)
name_entry.place(relx=0.6, rely=0.1, anchor=CENTER)

psw_lbl = Label(root, text="Password")
psw_lbl.place(relx=0.4, rely=0.2, anchor=CENTER)

psw_entry = Entry(root)
psw_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

captcha_lbl = Label(root, text="Captcha")
captcha_lbl.place(relx=0.4, rely=0.3, anchor=CENTER)

captcha_entry = Entry(root)
captcha_entry.place(relx=0.6, rely=0.3, anchor=CENTER)

updated_name = Label(root)
updated_name.place(relx=0.5, rely=0.7, anchor=CENTER)

updated_psw = Label(root)
updated_psw.place(relx=0.5, rely=0.8, anchor=CENTER)

updated_captcha = Label(root)
updated_captcha.place(relx=0.5, rely=0.9, anchor=CENTER)

class UserDB():
    def __init__(self):
        self.__username = "jerry"
        self.__password = "tom@#31nbdj"
        self.captcha = "@##$$@@4"

    def show_user(self):
        updated_name["text"]= "Name : " + self.__username
        updated_psw["text"]= "Password : " + self.__password
        updated_captcha["text"]= "Captcha : " + self.captcha

    def add_user1( self,name,password):
        self.__username = name
        self.__password = password

user = UserDB()


def add_user():
    user.username = name_entry.get()
    user.password = psw_entry.get() 
    user.captcha = captcha_entry.get()
    user.add_user1(name_entry.get(), psw_entry.get())




add_btn = Button(root, text = "Update Login Details", command = add_user)
add_btn.place(relx = 0.4, rely = 0.5, anchor = CENTER)

show_btn = Button(root, text = "Show Profile", command = user.show_user)
show_btn.place(relx = 0.6, rely = 0.5, anchor = CENTER)

root.mainloop()

