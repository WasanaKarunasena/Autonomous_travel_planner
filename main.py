from agents.coordinator_agent import CoordinatorAgent

if __name__ == "__main__":
    agent = CoordinatorAgent()
    plan = agent.plan_trip(
        origin="NYC", destination="Paris", date="2025-09-20",
        nights=3, budget=1000
    )
    print("\nFinal Travel Plan:\n", plan)
