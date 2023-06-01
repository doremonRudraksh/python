from tkinter import *
import requests
import json

root = Tk()
root.title("BBC News Update")
root.geometry("900x600")
root.config(bg = "white")


label_heading = Label(root,text="BBC NEWS UPDATE",bg="white",fg="blue",font=("bold",15))
label_heading.place(relx=0.5,rely=0.05,anchor=CENTER)

news_1_title = Label(root,font=("italic",10),bg="black",fg="red",justify=LEFT)
news_1_title.place(relx=0.5,rely=0.1,anchor=CENTER)

news_description1_lbl = Label(root, font = ("arial", 10, "bold"), fg = "black", bg = "white", wraplength = 900, justify = LEFT)
news_description1_lbl.place(relx = 0.5, rely = 0.2, anchor = CENTER)

news_2_title = Label(root,font=("italic",10),bg="black",fg="red",justify=LEFT)
news_2_title.place(relx=0.5,rely=0.3,anchor=CENTER)

news_description2_lbl = Label(root, font =( "arial", 10, "bold"), fg = "black", bg = "white", wraplength = 900, justify = LEFT)
news_description2_lbl.place(relx = 0.5, rely = 0.4, anchor = CENTER)

news_3_title = Label(root,font=("italic",10),bg="black",fg="red",justify=LEFT)
news_3_title.place(relx=0.5,rely=0.5,anchor=CENTER)

news_description3_lbl = Label(root, font = ("arial", 10, "bold"), fg = "black", bg = "white", wraplength = 900, justify = LEFT)
news_description3_lbl.place(relx = 0.5, rely = 0.6, anchor = CENTER)


news_4_title = Label(root,font=("italic",10),bg="black",fg="red",justify=LEFT)
news_4_title.place(relx=0.5,rely=0.7,anchor=CENTER)

news_description4_lbl = Label(root, font =( "arial", 10, "bold"), fg = "black", bg = "white", wraplength = 900, justify = LEFT)
news_description4_lbl.place(relx = 0.5, rely = 0.8, anchor = CENTER)

news_5_title = Label(root,font=("italic",10),bg="black",fg="red",justify=LEFT)
news_5_title.place(relx=0.5,rely=0.9,anchor=CENTER)

news_description5_lbl = Label(root, font =( "arial", 10, "bold"), fg = "black", bg = "white", wraplength = 900, justify = LEFT)
news_description5_lbl.place(relx = 0.5, rely = 0.95, anchor = CENTER)

def getNews():
    api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=64137e2ba938419fb69e343d94074536")
    api_output_json = json.loads(api_request.content)
    
    news_title1 = api_output_json["articles"][1]["title"]
    news_description1 = api_output_json["articles"][1]["description"]

    news_title2 = api_output_json["articles"][3]["title"]
    news_description2 = api_output_json["articles"][3]["description"]

    news_title3 = api_output_json["articles"][5]["title"]
    news_description3 = api_output_json["articles"][5]["description"]

    news_title4 = api_output_json["articles"][7]["title"]
    news_description4 = api_output_json["articles"][7]["description"]

    news_title5 = api_output_json["articles"][9]["title"]
    news_description5 = api_output_json["articles"][9]["description"]
    
    news_1_title["text"] = "Title : " + news_title1
    news_description1_lbl["text"] = "Description : " + news_description1

    news_2_title["text"] = "Title : " + news_title2
    news_description2_lbl["text"] = "Description : " + news_description2

    news_3_title["text"] = "Title : " + news_title3
    news_description3_lbl["text"] = "Description : " + news_description3

    news_4_title["text"] = "Title : " + news_title4
    news_description4_lbl["text"] = "Description : " + news_description4

    news_5_title["text"] = "Title : " + news_title5
    news_description5_lbl["text"] = "Description : " + news_description5

getNews()

root.mainloop()

