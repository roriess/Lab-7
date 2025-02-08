from tkinter import *
import json
import requests

window = Tk()
window.title("Weather forecast for your city")
window.geometry('450x250')

lbl0 = Label(window, text="Weather forecast for your city", font=("Arial Bold", 25))  
lbl0.grid(column=0, row=0) 

lbl1 = Label(window, text="Enter your city", font=("Arial Bold", 12))  
lbl1.grid(column=0, row=1) 

lbl2 = Label(window, text="(For example, London)", font=("Arial Bold", 10))  
lbl2.grid(column=0, row=2) 

txt = Entry(window, width=10)
txt.grid(column=0, row=3) 

def clicked():   
    city_name = txt.get()
    key = "dab973f7b489d6d71c5e519d318a5526"

    response = requests.post(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric")
    result = json.loads(response.text)

    temp = result['main']['temp']
    humidity = result['main']['humidity']
    pressure = result['main']['pressure']

    temp_output = f"{'Temp:'} {temp} {'degrees Celsius'}"
    humidity_output = f"{'Humidity:'} {humidity}"
    pressure_output = f"{'Pressure:'} {pressure}"

    lbl_temp = Label(window, text=temp_output, font=("Arial Bold", 10))  
    lbl_temp.grid(column=0, row=5) 

    lbl_humidity = Label(window, text=humidity_output, font=("Arial Bold", 10))  
    lbl_humidity.grid(column=0, row=6) 

    lbl_pressure = Label(window, text=pressure_output, font=("Arial Bold", 10))  
    lbl_pressure.grid(column=0, row=7) 

    lbl_pressure = Label(window, text="good luck;)", font=("Arial Bold", 10))  
    lbl_pressure.grid(column=0, row=8) 

btn = Button(window, text="Find out the weather", bg="white", fg="black", command=clicked)
btn.grid(column=0, row=4) 
 
window.mainloop()