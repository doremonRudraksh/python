from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root=Tk()
root.configure(background="blue")
root.title("Language Translator")
root.geometry("500x500")

languages = list(LANGUAGES.values())    

lbl_title = Label(root, text="Language Translator", fg="Red", font = ("Curlz MT",15,"italic"))
lbl_title.place(relx=0.5, rely=0.1, anchor=CENTER)


lbl_enter_text = Label(root, text="Enter Text", fg="Black", font = ("Comic Sans MS",15,"italic"))
lbl_enter_text.place(relx=0.1, rely=0.3, anchor=CENTER)

input_text = Text(root, bg="white", font=("Comic Sans MS",15,"italic"),height=7 ,width=40,padx=3,pady=3,bd=0)
input_text.place(relx=0.4,rely=0.6,anchor=E)

dropdown_imput = ttk.Combobox(root,state="readonly", values=languages)
dropdown_imput.place(relx=0.2,rely=0.3,anchor=W)
dropdown_imput.set("english")

output_label = Label(root,text="Output",bg="white", font=("Comic Sans MS",15,"italic"))
output_label.place(relx=0.7,rely=0.3,anchor=E)

output_text = Text(root, bg="white", font=("Comic Sans MS",15,"italic"),height=7 ,width=40,padx=3,pady=3,bd=0)
output_text.place(relx=0.9,rely=0.6,anchor=E)

dropdown_output = ttk.Combobox(root,state="readonly", values=languages)
dropdown_output.place(relx=0.9,rely=0.3,anchor=E, width=200)
dropdown_output.set("Choose Output Language")

def translators():
    translator = Translator()
    print(dropdown_imput.get())
    print(dropdown_output.get())
    print(input_text.get(1.0,END))

    try:
        translated =translator.translate(text=input_text.get(1.0,END),src = dropdown_imput.get(),dest = dropdown_output.get())
        output_text.delete(1.0,END)
        output_text.insert(END,translated.text)

    except:
        print("try again")



btn=Button(root, text="Translate", command=translators ,font=("Comic Sans MS",10,"bold","italic"),bg="white",fg="black",activebackground="red",relief=FLAT,pady=2)
btn.place(relx=0.47,rely=0.8,anchor=CENTER)

label_footer = Label(root,text="CREATED BY RUDRAKSH SHARMA",font=("Juice ITC",10,"bold"))
label_footer.place(relx=0.47,rely=1,anchor=S)



root.mainloop()