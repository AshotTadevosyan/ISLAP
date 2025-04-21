import joblib
from algorithms.levenshtein import levenshtein_score
from algorithms.soundex import soundex_score
from algorithms.jaro_winkler import jaro_winkler_score
from algorithms.token import jaccard_similarity
from algorithms.embedding import embedding_score

import os

model_path = os.path.join(os.path.dirname(__file__), "similarity_model.pkl")
model = joblib.load(model_path)

def predict_score(name1, name2):
    features = [
        levenshtein_score(name1, name2),
        soundex_score(name1, name2),
        jaro_winkler_score(name1, name2),
        jaccard_similarity(name1, name2),
        embedding_score(name1, name2),
    ]
    return model.predict_proba([features])[0][1]