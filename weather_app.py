# Import necessary libraries
import requests
import json
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# API Key and base URL for the weather service
api_key = 'e6a1ae4445897b00576e0d3939d388dc'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

# Function to retrieve weather data when the button is clicked
def get_weather():
    # Get city name from user input
    city = city_entry.get()
    # Prepare parameters for the API call
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    # Make API call to OpenWeatherMap service
    response = requests.get(base_url, params=params)

    # Check if the API call was successful
    if response.status_code == 200:
        try:
            # Parse JSON data from the API response
            data = response.json()

            # Extract relevant weather information from the JSON data
            temperature = data.get('main', {}).get('temp', 'N/A')
            weather_desc = data.get('weather', [{}])[0].get('description', 'N/A')
            icon_code = data.get('weather', [{}])[0].get('icon', '')

            # Update labels with weather information
            temperature_label.config(text=f'Temperature: {temperature}°C')
            weather_desc_label.config(text=f'Weather: {weather_desc}')

            # Display weather icon using Pillow library
            if icon_code:
                icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'
                image = Image.open(requests.get(icon_url, stream=True).raw)
                photo = ImageTk.PhotoImage(image)
                icon_label.config(image=photo)
                icon_label.photo = photo

            # Calculate local time using timezone information from the API response
            timezone_offset = data.get('timezone', 0)
            current_utc_time = datetime.utcnow()
            local_time = current_utc_time + timedelta(seconds=timezone_offset)
            local_time_str = local_time.strftime('%Y-%m-%d %H:%M:%S')

            # Update label with local time
            time_label.config(text=f'Local Time: {local_time_str}')

        # Handle JSON decoding error
        except json.JSONDecodeError:
            temperature_label.config(text='Error: Invalid JSON response')
    else:
        # Handle API request failure
        temperature_label.config(text=f'Error: API request failed (Status Code: {response.status_code})')

# Create the main GUI window
root = tk.Tk()
root.title('Weather App')

# Create GUI elements (labels, entry, button)
city_label = Label(root, text='Enter City:')
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
get_weather_button = Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()
temperature_label = Label(root, text='')
temperature_label.pack()
weather_desc_label = Label(root, text='')
weather_desc_label.pack()
icon_label = Label(root)
icon_label.pack()
time_label = Label(root, text='')
time_label.pack()

# Start the GUI main loop
root.mainloop()
