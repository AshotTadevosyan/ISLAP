import jellyfish

def jaro_winkler_score(s1, s2):
    return jellyfish.jaro_winkler_similarity(s1, s2)
