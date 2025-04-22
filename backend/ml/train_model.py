import sqlite3
import random
import pickle
from backend.algorithms.levenshtein import levenshtein_score
from backend.algorithms.soundex import soundex_score
from backend.algorithms.jaro_winkler import jaro_winkler_score
from backend.algorithms.token import jaccard_similarity
from backend.algorithms.embedding import embedding_score

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def load_real_pairs(db_path, sample_size=300):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM sanctions")
    rows = cursor.fetchall()
    conn.close()

    full_names = [f"{first} {last}".strip() for first, last in rows if first and last]
    full_names = list(set(full_names))
    random.shuffle(full_names)

    real_pairs = [(a, b, 1) for a, b in zip(full_names[::2], full_names[1::2])][:sample_size]
    return real_pairs


def generate_fake_pairs(full_names, sample_size=300):
    fake_pairs = []
    for _ in range(sample_size):
        a, b = random.sample(full_names, 2)
        fake_pairs.append((a, b, 0))
    return fake_pairs


def extract_features(name1, name2):
    return [
        levenshtein_score(name1, name2),
        soundex_score(name1, name2),
        jaro_winkler_score(name1, name2),
        jaccard_similarity(name1, name2),
        embedding_score(name1, name2)
    ]


def main():
    db_path = "backend/data/sanctions.db"  
    real = load_real_pairs(db_path)
    names = [name for pair in real for name in pair[:2]]
    fake = generate_fake_pairs(names)

    all_pairs = real + fake
    random.shuffle(all_pairs)

    X = [extract_features(a, b) for a, b, _ in all_pairs]
    y = [label for _, _, label in all_pairs]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    with open("backend/ml/similarity_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model trained and saved.")


if __name__ == "__main__":
    main()