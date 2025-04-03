from algorithms.scorer import combined_score
from algorithms.utility import normalize

def find_best_matches(input_name, db_records, country="", sanction_id="", threshold=0.6, limit=5):
    matches = []
    input_name = normalize(input_name)

    for full_name, db_country, db_id in db_records:
        if country and country.lower() not in db_country.lower():
            continue

        if sanction_id and sanction_id.lower() not in db_id.lower():
            continue

        normalized_name = normalize(full_name)
        score = combined_score(input_name, normalized_name)

        if score >= threshold:
            matches.append((full_name, db_country, db_id, score))

    matches.sort(key=lambda x: x[3], reverse=True)
    return matches[:limit]