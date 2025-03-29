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

├── README.md               # Project overview and instructions
├── identifier.sqlite       # SQLite database for storing sanctions data
├── main.py                 # Main entry point for the application
├── parser/                 # Directory for parsing modules
│   └── xml_parser.py       # XML parsing logic
├── search/                 # Directory for search modules
│   └── search_engine.py    # Search engine logic
├── scoring/                # Directory for scoring modules
│   ├── jaro_winkler.py     # Jaro-Winkler algorithm implementation
│   ├── levenshtein.py      # Levenshtein distance algorithm implementation
│   └── soundex.py          # Soundex algorithm implementation
└── utils/                  # Directory for utility modules
    └── database.py         # Database interaction logic
