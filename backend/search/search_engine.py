from backend.algorithms.scorer import combined_score
from backend.algorithms.utility import normalize_name

def find_best_matches(input_name, db_records, threshold=0.6):
    input_name = normalize_name(input_name)
    matches = []

    if len(input_name) >= 5:
        for record in db_records:
            name = normalize_name(record["name"])
            if input_name in name:
                match = record.copy()
                match["score"] = 1.0  
                matches.append(match)

        if matches:
            return matches  

    for record in db_records:
        name = normalize_name(record["name"])
        score = combined_score(input_name, name)
        if score >= threshold:
            match = record.copy()
            match["score"] = score
            matches.append(match)

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches[:5]