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
├── algorithms/         # Scoring algorithms
│   ├── jaro_winkler.py
│   ├── levenshtein.py
│   ├── soundex.py
│   └── scorer.py
├── cli/                # CLI entry point
│   └── main.py
├── data/               # XML file and database converter
│   ├── sanctions_list.XML
│   └── xml_to_sqlite.py
├── search/             # Search engine and DB loading logic
│   ├── db_loader.py
│   └── search_engine.py
├── identifier.sqlite   # Generated SQLite DB of parsed entities
├── venv/               # (optional) Virtual environment
└── README.md 

---


