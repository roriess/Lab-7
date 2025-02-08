import tkinter as tk
from PIL import ImageTk, Image
import urllib.request
import io
import requests

def display_image_from_url(url):
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    window = tk.Tk()
    window.title("Photo of the day from Nasa")

    lbl = tk.Label(window, text="Photo of the day from Nasa", font=("Arial Bold", 25))  
    lbl.grid(column=0, row=0) 

    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image) 

    label = tk.Label(window, image=photo)
    label.image = photo
    label.grid(column=0, row=1)
    
    window.mainloop()

key = ""
response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
result = response.json()

display_image_from_url(result['hdurl'])