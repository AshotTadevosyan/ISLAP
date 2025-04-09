from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches

from algorithms.levenshtein import levenshtein_score
from algorithms.soundex import soundex_score
from algorithms.jaro_winkler import jaro_winkler_score
from algorithms.token import jaccard_similarity
from algorithms.embedding import embedding_score
from algorithms.scorer import combined_score

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

records = load_names_from_db()

@app.get("/search")
def search(name: str = Query(..., min_length=3), threshold: float = 0.6):
    results = find_best_matches(name, records, threshold)
    return [
        {
            "name": r["name"],
            "score": round(r["score"] * 100, 2),
            "country": r["country"],
            "date_of_birth": r["date_of_birth"],
            "program": r["program"],
            "is_organization": r["is_organization"]
        }
        for r in results
    ]

@app.get("/benchmark")
def benchmark(name1: str, name2: str):
    return {
        "levenshtein": round(levenshtein_score(name1, name2), 4),
        "soundex": round(soundex_score(name1, name2), 4),
        "jaro_winkler": round(jaro_winkler_score(name1, name2), 4),
        "jaccard": round(jaccard_similarity(name1, name2), 4),
        "embedding": round(embedding_score(name1, name2), 4),
        "combined_score": round(combined_score(name1, name2), 4),
    }

build_path = Path(__file__).resolve().parent.parent / "build"
# app.mount("/", StaticFiles(directory=build_path, html=True), name="static")``