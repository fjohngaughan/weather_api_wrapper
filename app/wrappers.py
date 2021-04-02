import requests
from datetime import datetime

class CityWeather:
    def __init__(self, city, current, hi, lo, feels_like, description, sunrise, sunset):
        self.city = city
        self.current = current
        self.hi = hi
        self.lo = lo
        self.feels_like = feels_like
        self.description = description
        self.sunrise = sunrise
        self.sunset = sunset

    def __str__(self):
        return f"City Weather: {self.city}"

    def __repr__(self):
        return f"City Weather | {self.city}"

class OpenWeatherAPI:
    def __init__(self):
        self.base_path = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = '24411d29be6cf60408be9637d4700443'

    # If you wanted to have the data from the api show up in multiple pages on the website without
    # hardcoding it into each route...   
    # def _get(self, url, data, headers):
    #     response = requests.get(url, headers=headers, data=data)
    #     return response.json()

    def get_city_weather_data(self, city):
        url = self.base_path + '?q=' + city + '&appid=' + self.api_key + '&units=imperial'
        response = requests.get(url)
        data = response.json()
        city = data['name']
        current = data['main']['temp']
        hi = data['main']['temp_max']
        lo = data['main']['temp_min']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        city_data = CityWeather(city, current, hi, lo, feels_like, description, sunrise, sunset)
        return city_data 


