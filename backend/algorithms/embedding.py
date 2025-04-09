from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedding_score(name1, name2):
    embeddings = model.encode([name1, name2], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return score.item()