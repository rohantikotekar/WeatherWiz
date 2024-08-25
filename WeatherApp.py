from tkinter import *
from PIL import ImageTk, Image
import requests
import time

def getWeather(event=None):
    city = city_entry.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=760eebf1acdb97450024e42b82c8fce5"
    json_data = requests.get(api).json() 
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']["pressure"]
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 19800))    
    final_info = condition + "\n" +"  " + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    my_canvas.create_text(590,530, text=final_info, font=("Gill Sans", 42, 'bold'), fill="white")
    my_canvas.create_text(140,630, text=final_data, font=("Futura", 21, 'bold'), fill="cyan")

def entry_clear(e):
    city_entry.delete(0, END)

root = Tk()
root.title("WEATHER APP")
root.config(bg="grey")
root.geometry("700x1280")
root.resizable(False, False)

# Load and resize the background image to match window size
bg_image_path = "C:/Users/ROHAN/Downloads/vector-damask-seamless-pattern-background-classical-luxury-old-fashioned-damask-ornament-royal-victorian-seamless-texture-wallpapers-textile-wrapping-exquisite-floral-baroque-template_1217-738.png"
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((700, 1280), Image.ANTIALIAS)  # Resize to match window dimensions
image_bg = ImageTk.PhotoImage(bg_image)

my_canvas = Canvas(root, width=700, height=1280, bd=0, highlightthickness=0) 
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=image_bg, anchor="nw")

my_canvas.create_text(350, 120, text="WEATHER APP", font=("Rockwell", 51, 'bold'), fill="gold")

city_entry = Entry(root, font=("Helvetica", 27, 'bold'), width=18, fg="black")
city_entry.insert(0, "Enter a City")
my_canvas.create_window(168, 200, anchor="nw", window=city_entry)
city_entry.bind("<Button-1>", entry_clear)
city_entry.bind("<Return>", getWeather)

root.mainloop()
