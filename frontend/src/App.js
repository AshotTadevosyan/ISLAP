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
      const res = await fetch(`/search?name=${encodeURIComponent(fullName)}`);
      const data = await res.json();
      const filtered = data.filter((match) => match.score >= threshold);
      setResults(filtered);
    } catch (err) {
      alert("Search failed. Is the backend running?");
    }
  };

  return (
    <div style={{
      fontFamily: "Segoe UI, sans-serif",
      backgroundColor: "#f9fafb",
      minHeight: "100vh",
      padding: "2rem",
      display: "flex",
      flexDirection: "column",
      alignItems: "center"
    }}>
      <div style={{
        backgroundColor: "#ffffff",
        padding: "2rem",
        borderRadius: "8px",
        boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
        width: "100%",
        maxWidth: "600px"
      }}>
        <h1 style={{ marginBottom: "1rem", fontSize: "1.75rem", textAlign: "center" }}>
          ISLAP – Sanctions Name Matcher
        </h1>

        <form onSubmit={handleSearch}>
          <div style={{ display: "flex", gap: "1rem", marginBottom: "1rem" }}>
            <input
              type="text"
              placeholder="First Name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="Last Name"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              style={inputStyle}
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

          <button type="submit" style={buttonStyle}>
            Search
          </button>
        </form>

        <ul style={{ marginTop: "2rem", paddingLeft: "1rem" }}>
          {results.length === 0 ? (
            <li style={{ color: "#999" }}>No matches found.</li>
          ) : (
            results.map((match, index) => (
              <li key={index} style={{ marginBottom: "0.5rem" }}>
                <strong>{match.name}</strong> – {match.score}%
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}

const inputStyle = {
  padding: "0.5rem",
  width: "100%",
  border: "1px solid #ccc",
  borderRadius: "4px",
  fontSize: "1rem"
};

const buttonStyle = {
  padding: "0.5rem 1rem",
  fontSize: "1rem",
  backgroundColor: "#0057ff",
  color: "#fff",
  border: "none",
  borderRadius: "4px",
  cursor: "pointer",
  width: "100%",
  marginTop: "0.5rem"
};

export default App;