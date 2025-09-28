from fastapi import FastAPI

app = FastAPI()

@app.get("/hotels")
def get_hotels(city: str, nights: int):
    hotels = [
        {"name": "Grand Hotel", "price": 120, "city": city},
        {"name": "Budget Inn", "price": 60, "city": city},
    ]
    return {"hotels": hotels}
