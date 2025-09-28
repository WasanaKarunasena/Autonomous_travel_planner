import requests

class WeatherAgent:
    def check_weather(self, city, date):
        r = requests.get("http://localhost:8004/weather", params={"city": city, "date": date})
        return r.json()
