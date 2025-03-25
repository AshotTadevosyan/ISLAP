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
├── algorithms/     
│   ├── jaro_winkler.py
│   ├── levenshtein.py
│   ├── soundex.py
│   └── scorer.py
├── cli/        
│   └── main.py
├── data/   
│   ├── sanctions_list.XML
│   └── xml_to_sqlite.py
├── search/  
│   ├── db_loader.py
│   └── search_engine.py
├── identifier.sqlit
└── README.md 
