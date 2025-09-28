from fastapi import FastAPI

app = FastAPI()

@app.post("/pay")
def make_payment(data: dict):
    return {"status": "success", "amount": data.get("amount")}
