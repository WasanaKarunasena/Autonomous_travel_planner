import requests

class FlightAgent:
    def search_flights(self, origin, destination, date):
        r = requests.get("http://localhost:8001/flights", params={
            "origin": origin, "destination": destination, "date": date
        })
        return r.json()["flights"]
