from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Diagnose Report")
root.geometry("540x540")
root.configure(background = "salmon")

question1_radioButton = StringVar(value="0")

question1 = Label(root, text="Do you expirience shortness of breath during routine activities ?" , fg = "white", bg = "salmon")
question1.pack()
question1_r1 = Radiobutton(root, text= "Yes", variable= question1_radioButton, value="Yes", bg="salmon")
question1_r1.pack()
question1_r2 = Radiobutton(root, text= "No", variable= question1_radioButton, value="No", bg="salmon")
question1_r2.pack()

question2_radioButton = StringVar(value="0")

question2 = Label(root, text="Do you swelling in feet/ankle/legs(schoes feel tighter) or abdomen ?", fg = "white", bg = "salmon")
question2.pack()
question2_r1 = Radiobutton(root, text= "Yes", variable= question2_radioButton, value="Yes", bg="salmon")
question2_r1.pack()
question2_r2 = Radiobutton(root, text= "No", variable= question2_radioButton, value="No", bg="salmon")
question2_r2.pack()

question3_radioButton = StringVar(value="0")

question3 = Label(root, text="Do you feel any symptoms - confusion , disorientation or loss of memory.  ?" , fg = "white", bg = "salmon")
question3.pack()
question3_r1 = Radiobutton(root, text= "Yes", variable= question3_radioButton, value="Yes", bg="salmon")
question3_r1.pack()
question3_r2 = Radiobutton(root, text= "No", variable= question3_radioButton, value="No", bg="salmon")
question3_r2.pack()

question4_radioButton = StringVar(value="0")

question4 = Label(root, text="Do you expirience shortness of breath while at rest. lying down ?" , fg = "white", bg = "salmon")
question4.pack()
question4_r1 = Radiobutton(root, text= "Yes", variable= question4_radioButton, value="Yes", bg="salmon")
question4_r1.pack()
question4_r2 = Radiobutton(root, text= "No", variable= question4_radioButton, value="No", bg="salmon")
question4_r2.pack()

question5_radioButton = StringVar(value="0")

question5 = Label(root, text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus ?" , fg = "white", bg = "salmon")
question5.pack()
question5_r1 = Radiobutton(root, text= "Yes", variable= question5_radioButton, value="Yes", bg="salmon")
question5_r1.pack()
question5_r2 = Radiobutton(root, text= "No", variable= question5_radioButton, value="No", bg="salmon")
question5_r2.pack()

def score1():
    score=0 
    if question1_radioButton.get() == "Yes":
        score = score+10
        print(score)

    if question2_radioButton.get() == "Yes":
        score = score+10
        print(score)

    if question3_radioButton.get() == "Yes":
        score = score+10
        print(score)

    if question4_radioButton.get() == "Yes":
        score = score+10
        print(score)

    if question5_radioButton.get() == "Yes":
        score = score+10
        print(score)

    if score <=10:
        messagebox.showinfo("Report", "You don't need to visit a doctor")

    elif score > 10 and score <= 30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")

btn = Button(root, text = "Show Report", command = score1)
btn.pack()

root.mainloop()

