import React, { useState } from "react";
import "./layout.css";

function App() {
  const [fullName, setFullName] = useState("");
  const [country, setCountry] = useState("");
  const [sanctionId, setSanctionId] = useState("");
  const [threshold, setThreshold] = useState(75);
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!fullName.trim()) {
      alert("Please enter a name.");
      return;
    }

    try {
      const res = await fetch(
        `/search?name=${encodeURIComponent(fullName)}&country=${encodeURIComponent(
          country
        )}&sanction_id=${encodeURIComponent(sanctionId)}`
      );
      if (!res.ok) throw new Error("Search failed");
      const data = await res.json();
      const filtered = data.filter((match) => match.score >= threshold);
      setResults(filtered);
    } catch (err) {
      console.error(err);
      alert("Search failed. Make sure the backend is running.");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">ISLAP – Sanctions Search</h1>
        <form onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Full Name"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            className="input"
          />
          <input
            type="text"
            placeholder="Country"
            value={country}
            onChange={(e) => setCountry(e.target.value)}
            className="input"
          />
          <input
            type="text"
            placeholder="Sanction ID"
            value={sanctionId}
            onChange={(e) => setSanctionId(e.target.value)}
            className="input"
          />
          <label className="threshold-label">
            Similarity Threshold: <strong>{threshold}%</strong>
          </label>
          <input
            type="range"
            min="50"
            max="100"
            value={threshold}
            onChange={(e) => setThreshold(parseInt(e.target.value))}
            className="slider"
          />
          <button type="submit" className="search-button">
            Search
          </button>
        </form>
        <ul className="results">
          {results.length > 0 ? (
            results.map((match, idx) => (
              <li key={idx}>
                <strong>{match.name}</strong> – {match.score}%
                <div>Country: {match.country}</div>
                <div>Sanction ID: {match.sanction_id}</div>
              </li>
            ))
          ) : (
            <li className="no-match">No matches found.</li>
          )}
        </ul>
      </div>
    </div>
  );
}

export default App;