import sqlite3
import random
import pandas as pd
from backend.algorithms.levenshtein import levenshtein_score
from backend.algorithms.soundex import soundex_score
from backend.algorithms.jaro_winkler import jaro_winkler_score
from backend.algorithms.token import jaccard_similarity
from backend.algorithms.embedding import embedding_score
from sklearn.linear_model import LogisticRegression
import joblib
import os

conn = sqlite3.connect("backend/data/sanctions.db") 
df = pd.read_sql_query("SELECT first_name, last_name FROM sanctions WHERE first_name IS NOT NULL AND last_name IS NOT NULL", conn)
conn.close()

df["full_name"] = df["first_name"].str.strip() + " " + df["last_name"].str.strip()
names = df["full_name"].dropna().unique().tolist()
names = [name for name in names if len(name.split()) > 1]

positive_samples = [(name, name, 1) for name in names]

random.shuffle(names)
half = len(names) // 2
negative_samples = [(names[i], names[i + half], 0) for i in range(half)]

samples = positive_samples + negative_samples
random.shuffle(samples)

def extract_features(name1, name2):
    return [
        levenshtein_score(name1, name2),
        soundex_score(name1, name2),
        jaro_winkler_score(name1, name2),
        jaccard_similarity(name1, name2),
        embedding_score(name1, name2),
    ]

X = []
y = []

for name1, name2, label in samples:
    try:
        X.append(extract_features(name1, name2))
        y.append(label)
    except Exception as e:
        print(f"Skipping ({name1}, {name2}) due to error: {e}")

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "backend/ml/similarity_model.pkl")  

print("Model training complete. Saved as similarity_model.pkl")