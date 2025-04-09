# ISLAP – International Sanctions List Approximate Processing

**ISLAP** is a search engine built for exploring international sanctions lists using intelligent approximate string matching algorithms, including traditional fuzzy logic and modern neural embeddings.

## Purpose

The goal of the project is to allow users to search for sanctioned individuals or organizations using inexact or partial information, handling:
- Spelling variations
- Transliteration differences
- Typo tolerance
- Semantic similarity (via transformer models)

---

## Run the Project Locally

## Features

Levenshtein, Soundex, Jaro-Winkler, Jaccard similarity
Neural similarity using SentenceTransformers (MiniLM)
Token-based matching for better partial results
Real-time suggestions (auto-complete)
Smart search threshold tuning
Benchmark route to compare algorithm performance

## Data Source

https://sanctionslist.ofac.treasury.gov/Home/ConsolidatedList

## Notes

sanctions.db is generated using the provided script and not included in this repo.

You can view or export it using tools like DB Browser for SQLite.

Core logic lives in:

	•	algorithms/: scoring functions
	•	search/: engine + database interface
	•	api/: FastAPI server
	•	frontend/: React app


# Credit

This project was developed as part of an internship at the Central Bank of Armenia