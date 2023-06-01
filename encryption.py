from tkinter import *
root=Tk()
root.title("Encryption")
root.configure(background ="black")
root.geometry("400x400")
enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)
label = Label(root, text="Name in Ascai", bg="red", fg="white")
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2 = Label(root, text="Encrypted name", bg="red", fg="white")
label2.place(relx=0.5, rely=0.7, anchor=CENTER)


def asciiConverter():
    input_word = str(enter_word.get())
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))

btn= Button(root, text="Display the ascii code and ecrypted name", command=asciiConverter, bg="white", fg="red")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

