from email import message
import string
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("fiver report")
root.geometry("600x600")

question1_radioButton = StringVar(value="0")

question1 = Label(root, text="Do you have headache and sore throat?")
question1.pack()
question1_r1 = Radiobutton(root, text= "Yes", variable= question1_radioButton, value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text= "No", variable= question1_radioButton, value="No")
question1_r2.pack()

question2_radioButton = StringVar(value="0")
question2= Label(root, text="Is your body temprature high ?")
question2.pack()
question2_r1 = Radiobutton(root, text="Yes", variable=question2_radioButton, value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text="No", variable=question2_radioButton, value="No" )
question2_r2.pack()

question3_radioButton = StringVar(value="0")
question3 = Label(root, text="Are their any symptom of redness in your eyes ?")
question3.pack()
question3_r1 = Radiobutton(root, text="Yes", variable=question3_radioButton, value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text="No", variable=question3_radioButton, value="No" )
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get() == "Yes":
        score = score+20
        print(score)

    if question2_radioButton.get() == "Yes":
        score = score+20
        print(score)

    if question3_radioButton.get() == "Yes":
        score = score+20
        print(score)

    if score <= 20:
        messagebox.showinfo("report", "You don't need to visit the doctor")

    elif score> 20 and score<=40:
        messagebox.showinfo("report", " You might have to perhaps visit the doctor")

    else:
        messagebox.showinfo("report", "I strongly advise you to vist the doctor")

btn = Button(root, text="Click me ", command=fever_score)
btn.pack()


root.mainloop()
