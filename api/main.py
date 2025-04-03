from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches

app = FastAPI()

names = load_names_from_db()

@app.get("/search")
def search(
    name: str = Query(..., min_length=3),
    country: str = Query("", alias="country"),
    sanction_id: str = Query("", alias="sanction_id"),
    threshold: float = Query(0.6)
):
    results = find_best_matches(name, names, country, sanction_id, threshold)
    return [
        {
            "name": r[0],
            "country": r[1],
            "sanction_id": r[2],
            "score": round(r[3] * 100, 2)
        }
        for r in results
    ]

build_path = Path(__file__).resolve().parent.parent / "build"
app.mount("/", StaticFiles(directory=build_path, html=True), name="static")