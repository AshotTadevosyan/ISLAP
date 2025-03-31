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
      alert("Please enter a name.");
      return;
    }

    try {
      const res = await fetch(`/search?name=${encodeURIComponent(fullName)}`);
      if (!res.ok) throw new Error("Search failed");

      const data = await res.json();
      const filtered = data.filter((match) => match.score >= threshold);
      setResults(filtered);
    } catch (err) {
      console.error(err);
      alert("Search failed. Make sure the backend is running and deployed correctly.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>ISLAP – Sanctions Search</h1>
        <form onSubmit={handleSearch}>
          <div style={styles.inputRow}>
            <input
              type="text"
              placeholder="First Name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              style={styles.input}
            />
            <input
              type="text"
              placeholder="Last Name"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              style={styles.input}
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

          <button type="submit" style={styles.button}>
            Search
          </button>
        </form>

        <ul style={styles.results}>
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

const styles = {
  container: {
    fontFamily: "Segoe UI, sans-serif",
    backgroundColor: "#f9fafb",
    minHeight: "100vh",
    padding: "2rem",
    display: "flex",
    justifyContent: "center",
  },
  card: {
    backgroundColor: "#ffffff",
    padding: "2rem",
    borderRadius: "8px",
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
    width: "100%",
    maxWidth: "600px",
  },
  title: {
    marginBottom: "1.5rem",
    fontSize: "1.75rem",
    textAlign: "center",
  },
  inputRow: {
    display: "flex",
    gap: "1rem",
    marginBottom: "1rem",
  },
  input: {
    padding: "0.5rem",
    flex: 1,
    border: "1px solid #ccc",
    borderRadius: "4px",
    fontSize: "1rem",
  },
  button: {
    padding: "0.5rem 1rem",
    fontSize: "1rem",
    backgroundColor: "#0057ff",
    color: "#fff",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
    width: "100%",
    marginTop: "0.5rem",
  },
  results: {
    marginTop: "2rem",
    paddingLeft: "1rem",
  },
};

export default App;