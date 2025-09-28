from fastapi import FastAPI

app = FastAPI()

@app.get("/flights")
def get_flights(origin: str, destination: str, date: str):
    flights = [
        {"airline": "AirX", "price": 450, "date": date, "origin": origin, "destination": destination},
        {"airline": "SkyJet", "price": 520, "date": date, "origin": origin, "destination": destination},
    ]
    return {"flights": flights}
