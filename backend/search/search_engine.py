from algorithms.scorer import combined_score
from algorithms.utility import normalize_name
from ml.predictor import predict_score

def find_best_matches(input_name, db_records, threshold=0.6, max_results=10, use_ml=True):
    input_name = normalize_name(input_name)
    matches = []

    if len(input_name) >= 5:
        for record in db_records:
            full_name = f"{record['first_name']} {record['last_name']}".lower()
            if input_name in full_name:
                match = record.copy()
                match["score"] = 1.0
                matches.append(match)

        if matches:
            return sorted(matches, key=lambda x: x["score"], reverse=True)[:max_results]

    for record in db_records:
        full_name = f"{record['first_name']} {record['last_name']}".lower()

        # Choose scoring method
        if use_ml:
            score = predict_score(input_name, full_name)
        else:
            score = combined_score(input_name, full_name)

        if score >= threshold:
            match = record.copy()
            match["score"] = round(score * 100, 2)
            matches.append(match)

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches[:max_results]