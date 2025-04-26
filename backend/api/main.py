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
from algorithms.utility import normalize_name
from ml.predictor import predict_score

app = FastAPI()

origins = [
    "https://islap.onrender.com",  
    "http://localhost:3000",      
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

records = load_names_from_db()

@app.get("/search")
def search(name: str = Query(..., min_length=3), threshold: float = 0.6, ml: bool = True):
    results = find_best_matches(name, records, threshold, use_ml=ml)
    return [
        {
            "name": r["name"],
            "score": r["score"],
            "country": r["country"],
            "date_of_birth": r["date_of_birth"],
            "program": r["program"],
            "is_organization": r["is_organization"]
        }
        for r in results
    ]


@app.get("/benchmark")
def benchmark(name1: str, name2: str):
    try:
        result = {
            "levenshtein": round(levenshtein_score(name1, name2), 4),
            "soundex": round(soundex_score(name1, name2), 4),
            "jaro_winkler": round(jaro_winkler_score(name1, name2), 4),
            "jaccard": round(jaccard_similarity(name1, name2), 4),
            "embedding": round(embedding_score(name1, name2), 4),
        }
        return {"success": True, "data": result}
    except Exception as e:
        print("Benchmark error:", e)
        return {"success": False, "error": str(e)}
    

    
build_path = Path(__file__).resolve().parents[2] / "build"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=10000, reload=False)