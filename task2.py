from tkinter import *
import json
import requests

window = Tk()
window.title("The most popular news about Apple now")

lbl0 = Label(window, text="The most popular news about Apple now", font=("Arial Bold", 25))  
lbl0.grid(column=0, row=0) 

def clicked():   
    key = ""

    params = {
        'country': 'us',
        'category': 'technology',
        'pageSize': 1
    }

    response = requests.get(f"https://newsapi.org/v2/top-headlines?country={params['country']}&category={params['category']}&pageSize={params['pageSize']}&apiKey={key}")
    result = response.json()

    for article in result['articles']:

        lbl_topic = Label(window, text=f"Topic: {article['title']}", font=("Arial Bold", 10))  
        lbl_topic.grid(column=0, row=2)

        lbl_resource = Label(window, text=f"Resource: {article['source']['name']}", font=("Arial Bold", 10))  
        lbl_resource.grid(column=0, row=3) 

        lbl_publication_date = Label(window, text=f"Publication date: {article['publishedAt'][:-10]}", font=("Arial Bold", 10))  
        lbl_publication_date.grid(column=0, row=4) 

        lbl_short_description = Label(window, text=f"Short description: {article['description']}", font=("Arial Bold", 10))  
        lbl_short_description.grid(column=0, row=5)  

btn = Button(window, text="Get information", bg="white", fg="black", command=clicked)
btn.grid(column=0, row=1) 

window.mainloop()