from fastapi import FastAPI

app = FastAPI()

@app.get("/weather")
def get_weather(city: str, date: str):
    return {"city": city, "date": date, "forecast": "Sunny", "temp": "24C"}
