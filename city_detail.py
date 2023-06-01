from tkinter import *
import requests
import json

root=Tk()
root.title("My city detail App")

root.geometry("250x250")
root.configure(background="blue")

lbl=Label(root,text="Capital City Name",bg="white",fg="Black",font=("helvetica",25,"bold"))
lbl.place(relx=0.1,rely=0.1,anchor=W)

entry = Entry(root)
entry.place(relx=0.1,rely=0.3,anchor=W)

country_lbl = Label(root, text = "Country:", bg = "blue", fg = "white", font = ("bold", 15))
country_lbl.place(relx = 0.1, rely = 0.5, anchor = W)

region_lbl = Label(root, text = "Region:", bg = "blue", fg = "white", font = ("bold", 15))
region_lbl.place(relx = 0.1, rely = 0.6, anchor = W)

area_lbl = Label(root, text = "Area:", bg = "blue", fg = "white", font = ("bold", 15))
area_lbl.place(relx = 0.1, rely = 0.7, anchor = W)

population_lbl = Label(root, text = "Population:", bg = "blue", fg = "white", font = ("bold", 15))
population_lbl.place(relx = 0.1, rely = 0.8, anchor = W)

language_lbl = Label(root, text = "Language:", bg = "blue", fg = "white", font = ("bold", 15))
language_lbl.place(relx = 0.1, rely = 0.9, anchor = W)

def city_detail():
    api_request = requests.get("https://restcountries.com/v2/capital/" +entry.get())
    api_output_json = json.loads(api_request.content)

    country =  api_output_json[0]["name"]
    print(country)

    country_lbl["text"] = "Country : " + str(country)

    language =  api_output_json[0]["languages"][0]["name"]
    print(language)

    language_lbl["text"] = "Language : " + str(language)

    area =  api_output_json[0]["area"]
    print(area)

    area_lbl["text"] = "Area : " + str(area)

    region =  api_output_json[0]["region"]
    print(region)

    region_lbl["text"] = "region: " + str(region)

    population =  api_output_json[0]["population"]
    print(population)

    population_lbl["text"] = "Population : " + str(population)

btn = Button(root, text="City Detail",relief=GROOVE,command=city_detail,bg="black",fg="red", font=("bold",25)
)
btn.place(relx=0.3,rely=0.3,anchor=W)

root.mainloop()



