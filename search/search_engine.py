from algorithms.scorer import combined_score

def find_best_matches(input_name, db_names, threshold=0.75):
    matches = []
    for name in db_names:
        score = combined_score(input_name, name)
        if score >= threshold:
            matches.append((name, score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:5]
