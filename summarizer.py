# summarizer.py

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import numpy as np

# Download punkt tokenizer if not already downloaded
nltk.download('punkt')

def extract_summary(text, num_sentences=5):
    """
    Extract a summary from the given text by selecting the most important sentences
    based on TF-IDF scoring.

    Args:
        text (str): The input text to summarize.
        num_sentences (int): Number of summary sentences to extract.

    Returns:
        list: List of selected important sentences as the summary.
    """

    # 1. Sentence Tokenization
    sentences = sent_tokenize(text)
    
    # If the text is too small, return all sentences
    if len(sentences) <= num_sentences:
        return sentences

    # 2. Calculate TF-IDF Matrix for the Sentences
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # 3. Compute sentence importance scores (sum of TF-IDF weights)
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).flatten()

    # 4. Get the indices of the top N sentences
    top_indices = sentence_scores.argsort()[-num_sentences:][::-1]

    # 5. Arrange top sentences in their original order
    top_sentences = [sentences[i] for i in sorted(top_indices)]

    return top_sentences
