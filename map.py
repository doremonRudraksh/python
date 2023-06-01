from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("World Clock")
root.geometry("1250x600")

india_map = ImageTk.PhotoImage(Image.open("india.jpg"))
us_map = ImageTk.PhotoImage(Image.open("usa.jpg"))
australia_map = ImageTk.PhotoImage(Image.open("australia.jpg"))
japan_map = ImageTk.PhotoImage(Image.open("japan.jpg"))

india_label = Label(root, text="India")
india_label.place(relx=0.3, rely=0.1, anchor=CENTER)


india_pm = Label(root)
india_pm["image"] = india_map
india_pm.place(relx = 0.3, rely = 0.2, anchor = CENTER)

india_time = Label(root)
india_time.palce(relx=0.3, rely=0.3, anchor=CENTER)

US_label = Label(root, text="USA")
US_label.place(relx=0.6, rely=0.1, anchor=CENTER)


US_pm = Label(root)
US_pm["image"] = us_map
US_pm.place(relx = 0.6, rely = 0.2, anchor = CENTER)

US_time = Label(root)
US_time.palce(relx=0.6, rely=0.3, anchor=CENTER)

aust_label = Label(root, text="Australia")
aust_label.place(relx=0.3, rely=0.6, anchor=CENTER)


aust_pm = Label(root)
aust_pm["image"] = australia_map
india_pm.place(relx = 0.3, rely = 0.7, anchor = CENTER)

aust_time = Label(root)
aust_time.palce(relx=0.3, rely=0.8, anchor=CENTER)

jap_label = Label(root, text="Japan")
jap_label.place(relx=0.6, rely=0.1, anchor=CENTER)


jap_pm = Label(root)
jap_pm["image"] = japan_map
jap_pm.place(relx = 0.6, rely = 0.2, anchor = CENTER)

jap_time = Label(root)
jap_time.place(relx=6.3, rely=0.3, anchor=CENTER)

class india():
    def time(self):
        home = pytz.timerzone("Asia/Kolkata")
        local_time =  datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200, self.time)

class usa():
    def time(self):
        home = pytz.timerzone("US/Central")
        local_time =  datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200, self.time)

class Japan():
    def time(self):
        home = pytz.timerzone("Japan'")
        local_time =  datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200, self.time)

class australia():
    def time(self):
        home = pytz.timerzone("Australia/ACT'")
        local_time =  datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200, self.time)


obj_india = india()
obj_usa = usa()
obj_australia = australia()
obj_japan = Japan()

india_btn = Button(root, text="shpw time", command=obj_india.time)
india_btn.place(relx = 0.3, rely = 0.4, anchor = CENTER)

us_btn = Button(root, text="shpw time", command=obj_usa.time)
us_btn.place(relx = 0.6, rely = 0.4, anchor = CENTER)

aust_btn = Button(root, text="shpw time", command=obj_australia.time)
aust_btn.place(relx = 0.3, rely = 0.9, anchor = CENTER)

japn_btn = Button(root, text="shpw time", command=obj_japan.time)
japn_btn.place(relx = 0.6, rely = 0.9, anchor = CENTER)

root.mainloop()



