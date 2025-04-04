from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches

app = FastAPI()

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

build_path = Path(__file__).resolve().parent.parent / "build"
app.mount("/", StaticFiles(directory=build_path, html=True), name="static")