import React, { useState } from "react";

function App() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [threshold, setThreshold] = useState(75);
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();

    const fullName = `${firstName} ${lastName}`.trim();
    if (!fullName) {
      alert("Please enter both first and last name.");
      return;
    }

    try {
      const res = await fetch(
        `http://localhost:8000/search?name=${encodeURIComponent(fullName)}`
      );
      const data = await res.json();

      const filtered = data.filter(match => match.score >= threshold);
      setResults(filtered);
    } catch (err) {
      alert("Search failed. Is the backend running?");
    }
  };

  return (
    <div style={{ fontFamily: "Arial", padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>ISLAP – Sanctions Name Matcher</h1>
      <form onSubmit={handleSearch} style={{ marginBottom: "1.5rem" }}>
        <div style={{ marginBottom: "0.75rem" }}>
          <input
            type="text"
            placeholder="First Name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            style={{ padding: "0.5rem", width: "47%", marginRight: "6%" }}
          />
          <input
            type="text"
            placeholder="Last Name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            style={{ padding: "0.5rem", width: "47%" }}
          />
        </div>

        <div style={{ marginBottom: "1rem" }}>
          <label>
            Similarity Threshold: <strong>{threshold}%</strong>
          </label>
          <input
            type="range"
            min="50"
            max="100"
            value={threshold}
            onChange={(e) => setThreshold(parseInt(e.target.value))}
            style={{ width: "100%" }}
          />
        </div>

        <button type="submit" style={{ padding: "0.5rem 1rem" }}>
          Search
        </button>
      </form>

      <ul>
        {results.length === 0 ? (
          <li>No matches found.</li>
        ) : (
          results.map((match, index) => (
            <li key={index}>
              {match.name} – Score: {match.score}%
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;