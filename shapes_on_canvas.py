from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Working On Canvas Using Functions")
root.geometry("1000x600")

label1 = Label(root, text="choose colour : ")
label1.place(relx=0.6 , rely= 0.9, anchor=CENTER)

canvas = Canvas(root, height= 490, width= 990, bg="white", highlightbackground="grey")
canvas.pack()



fill_color = ["Blue", "Green", "Red", "Yellow"]
color_dropdown = ttk.Combobox(root, state = "readonly", values = fill_color, width = 10)
color_dropdown.place(relx = 0.8, rely = 0.9, anchor = CENTER)

coordinates_values = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

startx = Label(root, text="Start =Y")
startx.place(relx=0.1, rely=0.85, anchor=CENTER)


d1 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
d1.place(relx = 0.2, rely = 0.85, anchor = CENTER)


starty = Label(root, text="Start -Y")
starty.place(relx=0.3, rely=0.85, anchor=CENTER)

d2 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
d2.place(relx = 0.4, rely = 0.85, anchor = CENTER)

endx = Label(root, text="End -X")
endx.place(relx=0.5, rely=0.85, anchor=CENTER)

d3 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
d3.place(relx = 0.6, rely = 0.85, anchor = CENTER)

endy = Label(root, text="End -Y")
endy.place(relx=0.7, rely=0.85, anchor=CENTER)

d3 = ttk.Combobox(root, state = "readonly", values = coordinates_values, width = 10)
d3.place(relx = 0.8, rely = 0.85, anchor = CENTER)

root.mainloop()
