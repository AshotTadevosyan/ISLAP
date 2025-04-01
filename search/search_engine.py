from algorithms.scorer import combined_score
from algorithms.utility import normalize  

def find_best_matches(input_name, db_names, threshold=0.6):
    matches = []
    input_name = normalize(input_name) 

    for name in db_names:
        normalized_name = normalize(name)  
        score = combined_score(input_name, normalized_name)

        if score >= threshold:
            matches.append((name, score))  

    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:5]