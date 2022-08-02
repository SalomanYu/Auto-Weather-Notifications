#!/usr/bin/python3.10   

from pyowm.owm import OWM
from datetime import datetime
import os
from your_place import city


def get_weather(place) -> float:
    try:
        owm = OWM('f2c53ec7f15d956f9f3beb17ddedff87')
        Manage = owm.weather_manager()
        Weather = Manage.weather_at_place(place)
        Temperature = Weather.weather
        return Temperature.temperature('celsius')['temp']

    except Exception as error:
        return error


def send_message(message: float | str) -> None:
    current_time = datetime.now().strftime('%H:%M')
    if isinstance(message, float):
        os.system(f"notify-send 'Weather at {current_time}' '{city}: {message}' ")
    else:
        error_text = str(message)
        match error_text:
            case 'Unable to find the resource':
                os.system(f"notify-send 'We`re have some problems...' '[ERROR] The city - {city} was not found' ")
            case _:
                os.system(f"notify-send 'We`re have some problems...' '[ERROR] Connection failed' ")

if __name__ == "__main__":
    result = get_weather(city)
    # print(result)
    send_message(result)
