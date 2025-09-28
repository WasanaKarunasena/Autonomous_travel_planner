from fastapi import FastAPI

app = FastAPI()

@app.post("/itinerary")
def create_itinerary(data: dict):
    return {"itinerary": data}
