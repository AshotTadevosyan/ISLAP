# ISLAP – International Sanctions List Approximation Processing

**ISLAP** is a modular Python project designed to parse and load sanctions data, store it in a local database, and allow advanced name-matching using multiple string similarity algorithms. It supports both automated parsing of XML-based data and interactive searching through a command-line interface.

---

## 📦 Features

- 📂 **Sanctions List Parser**: Converts XML-based watchlists into an SQLite database.
- 🔍 **Search Engine**: Finds similar names using fuzzy string matching.
- 📊 **Scoring Engine**: Ranks matches using multiple algorithms:
  - Jaro-Winkler
  - Levenshtein Distance
  - Soundex
  - Combined weighted scoring
  - Modular structure for easy maintenance and scaling

---

## 🗂️ Project Structure

ISLAP1/
├── api/                   
│   └── main.py          
├── build/                 
├── data/                   
│   └── sanctions.db       
│   └── xml_to_sqlite.py   
├── frontend/                 
│   └── src/App.js       
├── algorithms/               
│   ├── jaro_winkler.py
│   ├── levenshtein.py
│   └── soundex.py
├── search/                
│   ├── search_engine.py
│   └── db_loader.py
├── .gitignore
├── README.md
├── requirements.txt
└── render.yaml           
