import React, { useState } from "react";
import axios from "axios";


export default function TripForm({ setPlan }) {
  const [form, setForm] = useState({
    origin: "",
    destination: "",
    date: "",
    nights: 1,
    budget: 1000,
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8010/plan_trip", form, {
        headers: {
          "Content-Type": "application/json",
        },
      });

      setPlan(res.data.plan); // match backend response
    } catch (err) {
      console.error("Error fetching plan:", err.response ? err.response.data : err.message);
      alert("Error fetching plan. Check backend logs.");
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <label>Origin: </label>
      <input type="text" name="origin" value={form.origin} onChange={handleChange} required />
      <br />

      <label>Destination: </label>
      <input type="text" name="destination" value={form.destination} onChange={handleChange} required />
      <br />

      <label>Date: </label>
      <input type="date" name="date" value={form.date} onChange={handleChange} required />
      <br />

      <label>Nights: </label>
      <input type="number" name="nights" value={form.nights} onChange={handleChange} required />
      <br />

      <label>Budget ($): </label>
      <input type="number" name="budget" value={form.budget} onChange={handleChange} required />
      <br />

      <button type="submit">Plan My Trip</button>
    </form>
  );
}
