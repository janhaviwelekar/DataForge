from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_chunks(query, documents, top_k=3):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([query] + documents)

    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]

    return [(documents[i], scores[i]) for i in top_indices]
