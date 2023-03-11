import requests
import os

KEY = os.environ["OPEN_WEATHER_KEY"]

city = input("Введите город: ")

GEO_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

weather = requests.Session()
weather.params["apikey"] = KEY

geo = weather.get(GEO_ENDPOINT, params = {
                            "q": city,
                             "limit": 1
}).json()[0]

lat, lon = geo["lat"], geo["lon"]

forecast = weather.get(FORECAST_ENDPOINT, params = {
                            "lat": lat,
                            "lon": lon,
                            "lang": "ru",
                            "units": "metric"
}).json()

temp = forecast["main"]
weather_2 = forecast["weather"][0]
cur_weather = str.title(weather_2["description"])

real_temp, feels_like, humidity = round(temp["temp"]), round(temp["feels_like"]), temp["humidity"]

print(f"""{real_temp}°C (Ощущается как {feels_like}°C)
{cur_weather}
Влажность: {humidity}%
""")
