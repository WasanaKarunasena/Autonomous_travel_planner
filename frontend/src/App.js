import React, { useState } from "react";
import TripForm from "./components/TripForm";
import PlanResult from "./components/PlanResult";

function App() {
  const [plan, setPlan] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Autonomous Travel Planner ✈️</h1>
      <TripForm setPlan={setPlan} />
      {plan && <PlanResult plan={plan} />}
    </div>
  );
}

export default App;
