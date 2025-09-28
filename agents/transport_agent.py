import requests

class TransportAgent:
    def search_transport(self, city):
        r = requests.get("http://localhost:8003/transport", params={"city": city})
        return r.json()["transport"]
