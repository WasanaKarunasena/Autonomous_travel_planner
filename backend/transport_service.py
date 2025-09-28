from fastapi import FastAPI

app = FastAPI()

@app.get("/transport")
def get_transport(city: str):
    transport = [
        {"mode": "Taxi", "price": 30, "city": city},
        {"mode": "Bus", "price": 5, "city": city},
    ]
    return {"transport": transport}
