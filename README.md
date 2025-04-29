# ISLAP – International Sanctions List Approximate Processing

**ISLAP** is a search engine built for exploring international sanctions lists using intelligent approximate string matching algorithms, including traditional fuzzy logic and modern neural embeddings.

## Purpose

The goal of the project is to allow users to search for sanctioned individuals or organizations using inexact or partial information, handling:
- Spelling variations
- Transliteration differences
- Typo tolerance
- Semantic similarity (via transformer models)

## Features

- Levenshtein, Soundex, Jaro-Winkler, Jaccard similarity
- Neural similarity using SentenceTransformers (MiniLM)
- Token-based matching for better partial results
- Machine Learning scoring with dynamic weights
- Real-time suggestions (auto-complete)
- Smart search threshold tuning
- Benchmark route to compare algorithm performance
- Visual comparison via charts

## Machine Learning Integration

A custom machine learning model was trained to learn how to best score name similarity using multiple classical algorithms as features.

- **Model type**: Scikit-learn RandomForestRegressor
- **Input features**: Levenshtein, Jaccard, Jaro-Winkler, Soundex, and Sentence-BERT scores
- **Training data**: Hand-labeled name variations extracted from real-world sanction lists
- **Usage**: Toggle ML scoring in the UI; if enabled, the ML model will generate the final score
- **Result**: Offers more tolerance to edge cases and improves relevance for semantically similar names

The model is serialized as `similarity_model.pkl` and loaded during backend runtime.

## Data Source

https://sanctionslist.ofac.treasury.gov/Home/ConsolidatedList

## Notes

The `sanctions.db` database is included and located in `backend/data/`.

You can view or export it using tools like **DB Browser for SQLite**.

Core logic lives in:

- `algorithms/`: scoring functions (rule-based and statistical)
- `search/`: search engine and matching logic
- `ml/`: ML training and prediction logic
- `api/`: FastAPI application and routes
- `frontend/`: React application UI

## Technologies Used

- **Backend**: FastAPI, SQLite, SentenceTransformers, Scikit-learn
- **Frontend**: React, Recharts, Axios
- **ML Model**: Random Forest Regressor trained on similarity data

## Deployment

Live version: https://islap.onrender.com/

Local development is available under the `local-dev` branch:
```bash
cd backend
uvicorn api.main:app --reload --port 10000

cd frontend
npm install
npm start

## Credit

This project was developed as part of an internship at the Central Bank of Armenia