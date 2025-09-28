import requests

class HotelAgent:
    def search_hotels(self, city, nights):
        r = requests.get("http://localhost:8002/hotels", params={
            "city": city, "nights": nights
        })
        return r.json()["hotels"]
