def jaccard_similarity(name1, name2):
    set1 = set(name1.lower().split())
    set2 = set(name2.lower().split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    if not union:
        return 0.0

    return len(intersection) / len(union)