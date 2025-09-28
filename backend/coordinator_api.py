from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.coordinator_agent import CoordinatorAgent

# Initialize FastAPI app
app = FastAPI()
agent = CoordinatorAgent()

# --- CORS settings to allow React frontend ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request schema ---
class TripRequest(BaseModel):
    origin: str
    destination: str
    date: str
    nights: int
    budget: float

# --- POST endpoint to plan trip ---
@app.post("/plan_trip")
def plan_trip(request: TripRequest):
    plan = agent.plan_trip(
        origin=request.origin,
        destination=request.destination,
        date=request.date,
        nights=request.nights,
        budget=request.budget
    )
    return {"plan": plan}
