
    # api_key = "cdf5db65dcd384ea5370ad59f4e71c28"

import requests
from tkinter import *
from tkinter import ttk

def get_weather():
    city = city_entry.get()
    api_key = "cdf5db65dcd384ea5370ad59f4e71c28"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        result_label.config(text=f"Weather: {weather}\nTemperature: {temp}°C")
    else:
        result_label.config(text="City not found!")

# GUI Setup
root = Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#f0f8ff")
root.iconbitmap("sun.ico")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TLabel", background="#f0f8ff", font=("Helvetica", 14))

ttk.Label(root, text="Enter City:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
city_entry = ttk.Entry(root, font=("Helvetica", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10)
ttk.Button(root, text="Get Weather", command=get_weather).grid(row=1, column=0, columnspan=2, pady=10)
result_label = ttk.Label(root, text="", anchor="center", background="#f0f8ff")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
