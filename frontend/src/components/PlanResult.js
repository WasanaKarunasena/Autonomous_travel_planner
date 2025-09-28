import React from "react";


export default function PlanResult({ plan }) {
  return (
    <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ccc" }}>
      <h2>Travel Plan</h2>
      <pre style={{ whiteSpace: "pre-wrap" }}>
        {typeof plan === "string" ? plan : JSON.stringify(plan, null, 2)}
      </pre>
    </div>
  );
}
