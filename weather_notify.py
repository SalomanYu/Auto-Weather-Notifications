#!/usr/bin/python3

from pyowm.owm import OWM
from datetime import datetime
import os
from your_place import city

# import sys
# city = sys.argv[1]


def get_weather(place):
    try:
        owm = OWM('f2c53ec7f15d956f9f3beb17ddedff87')
        Manage = owm.weather_manager()
        Weather = Manage.weather_at_place(place)
        Temperature = Weather.weather
        return Temperature.temperature('celsius')['temp']

    except Exception as error:
        return error


def send_message(message: str):
    current_time = datetime.now().strftime('%H:%M')

    if 'Unable to find the resource' in str(message):
        os.system("notify-send 'Failed Weather app' 'The city was not found' ")

    elif 'Failed to establish a new connection' in str(message):
        os.system("notify-send 'Failed Weather app' 'Check internet-connection' ")    
    
    else:
        os.system(f"notify-send 'Weather in {current_time}' '{city}: {Error}' ")


result = get_weather(city)
send_message(result)
