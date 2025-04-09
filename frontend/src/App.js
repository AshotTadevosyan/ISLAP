import React, { useState } from "react";
import "./layout.css";
import ShapeImg from "./shape.png";
import Axios from "axios";

const PROGRAM_LINKS = {
  "NS-PLC": "https://ofac.treasury.gov/media/10411/download?inline",
  "UKRAINE-EO13662": "https://ofac.treasury.gov/sanctions-programs-and-country-information/ukraine-russia-related-sanctions",
  "RUSSIA-EO14024": "https://ofac.treasury.gov/faqs/topic/6626",
  "FSE-IR": "https://ofac.treasury.gov/recent-actions/fse_list_intro",
  "CAATSA - RUSSIA": "https://ofac.treasury.gov/sanctions-programs-and-country-information/countering-americas-adversaries-through-sanctions-act-related-sanctions",
  "VENEZUELA-EO13850": "https://ofac.treasury.gov/faqs/topic/1581",
  "CMIC-EO13959": "https://ofac.treasury.gov/faqs/topic/5671",
  "BURMA-EO14014": "https://home.treasury.gov/news/press-releases/jy1701",
  "ILLICIT-DRUGS-EO14059": "https://ofac.treasury.gov/recent-actions/20221219",
};

function App() {
  const [fullName, setFullName] = useState("");
  const [threshold, setThreshold] = useState(80);
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    console.log(fullName)
    e.preventDefault();
    if (!fullName.trim()) return;

    try {
      const response = await Axios.get(
        `${process.env.REACT_APP_API_URL}/https://api.render.com/deploy/srv-cvkpga24d50c73du95c0?key=CFDjXvp1Uv8`,
        {
          params: {
            name: fullName,
            threshold: threshold / 100,
          },
        }
      );
      const data = response.data
      setResults(data);
    } catch (error) {
      console.error("Search failed", error);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">International Sanctions List Search Engine</h1>
        <form onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Search for a person or organization..."
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            className="input"
          />
          <label className="threshold-label">
            Minimum Score: <strong>{threshold}%</strong>
          </label>
          <input
            type="range"
            min="50"
            max="100"
            value={threshold}
            onChange={(e) => setThreshold(parseInt(e.target.value))}
            className="slider small-slider"
            style={{ width: "100%" }}
          />
          <button type="submit" className="search-button">
            Search
          </button>
          <button
            type="button"
            className="reset-button"
            onClick={() => {
              setFullName("");
              setThreshold(80);
              setResults([]);
            }}
          >
            Reset
          </button>
          <p className="info-text">
            Note: The search is case-insensitive and will match partial names.
          </p>
        </form>
        <ul className="results">
          {results.length > 0 ? (
            results.map((match, idx) => (
              <li key={idx} className="result-item">
                <strong>{match.name}</strong>
                {match.is_organization && <span className="tag">Organization</span>}
                <span className="score-tag">{match.score}%</span>
                <div className="details">
                  Country: {match.country || "N/A"} | Date of Birth: {match.date_of_birth || "N/A"} |
                  Link: {PROGRAM_LINKS[match.program] ? (
                    <a
                      href={PROGRAM_LINKS[match.program]}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {match.program}
                    </a>
                  ) : (
                    match.program || "N/A"
                  )}
                </div>
              </li>
            ))
          ) : (
            <li className="no-match">No matches found.</li>
          )}
        </ul>
      </div>
      <aside>
        <img src={ShapeImg} alt="Shape" />
      </aside>
    </div>
  );
}

export default App;
