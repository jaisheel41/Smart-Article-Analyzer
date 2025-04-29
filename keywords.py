# keywords.py

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords(text, top_n=10):
    """
    Extract top N keywords from text using TF-IDF scoring.
    """

    # TF-IDF vectorizer configuration
    vectorizer = TfidfVectorizer(stop_words='english', smooth_idf=True)


    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()

    # Sum TF-IDF scores for each feature (word)
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    top_indices = np.argsort(tfidf_scores)[-top_n:][::-1]
    
    keywords = [(feature_names[i], tfidf_scores[i]) for i in top_indices]

    return keywords
