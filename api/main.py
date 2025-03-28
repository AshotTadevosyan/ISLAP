from fastapi import FastAPI, Query
from search.db_loader import load_names_from_db
from search.search_engine import find_best_matches

app = FastAPI()
names = load_names_from_db()

@app.get("/search")
def search(name: str = Query(..., min_length=3)):
    results = find_best_matches(name, names)
    return [{"name": r[0], "score": round(r[1]*100, 2)} for r in results]

