from agents.flight_agent import FlightAgent
from agents.hotel_agent import HotelAgent
from agents.transport_agent import TransportAgent
from agents.weather_agent import WeatherAgent
from agents.payment_agent import PaymentAgent
from agents.ollama_client import query_ollama
import json

class CoordinatorAgent:
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.transport_agent = TransportAgent()
        self.weather_agent = WeatherAgent()
        self.payment_agent = PaymentAgent()

    def plan_trip(self, origin, destination, date, nights, budget):
        flights = self.flight_agent.search_flights(origin, destination, date)
        hotels = self.hotel_agent.search_hotels(destination, nights)
        transport = self.transport_agent.search_transport(destination)
        weather = self.weather_agent.check_weather(destination, date)

        prompt = f"""
        You are a travel planner. Use the following information to create a trip plan:
        - Flights: {flights}
        - Hotels: {hotels}
        - Transport: {transport}
        - Weather: {weather}
        - Budget: {budget}

        Respond ONLY in valid JSON format (no markdown fences, no text).
        JSON schema:
        {{
          "flight": {{...}},
          "hotel": [...],
          "transport": [...],
          "weather": {{...}},
          "total_cost": number,
          "summary": "string"
        }}
        """

        raw_plan = query_ollama(prompt).strip()

        # --- Step 1: remove code fences if any ---
        if raw_plan.startswith("```"):
            raw_plan = raw_plan.split("```")[1]
            raw_plan = raw_plan.replace("json", "").replace("python", "").strip()

        # --- Step 2: try parsing JSON directly ---
        try:
            plan = json.loads(raw_plan)
        except Exception:
            plan = {"summary": raw_plan}

        # --- Step 3: handle double-encoded JSON ---
        if isinstance(plan, str):
            try:
                plan = json.loads(plan)
            except Exception:
                plan = {"summary": plan}

        # --- Step 4: handle "summary" being a JSON string ---
        if isinstance(plan.get("summary"), str):
            try:
                inner = json.loads(plan["summary"])
                if isinstance(inner, dict) and "flight" in inner:
                    plan = inner
            except Exception:
                pass

        return plan
