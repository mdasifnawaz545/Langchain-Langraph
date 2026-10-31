import os

import requests
from pydantic import BaseModel

class get_weather(BaseModel):
    city: str
    temperature_celsius: str
    feels_like_celsius: str
    description: str
    humidity_percent: str

api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str)-> str:
    """ This function is used to call an API in order to get the about the weather by taking an input of the city from the user"""

        
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key, "units": "metric"},
        timeout=10,
    )
    if response.ok:
        weather = response.json()
        return {
            "city": weather.get("name", city),
            "temperature_celsius": weather.get("main", {}).get("temp"),
            "feels_like_celsius": weather.get("main", {}).get("feels_like"),
            "description": weather.get("weather", [{}])[0].get("description"),
            "humidity_percent": weather.get("main", {}).get("humidity"),
        }