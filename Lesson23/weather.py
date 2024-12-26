from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import sys

load_dotenv()

def get_current_weather(city="chittagong"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n*** Welcome to Weather App ***\n")
    city = input("Enter City: ")

    if not bool(city.strip()):
        city = "chittagong"

    if 'message' in get_current_weather(city):
        print("\nCity doesn't exist, try again later.\n")
        sys.exit()

    pprint(get_current_weather(city))
