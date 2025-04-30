# keywords.py

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# Load model once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
kw_model = KeyBERT(model=embed_model)

def extract_keywords(text, top_n=10, method='maxsum'):
    """
    Extract top keywords or phrases using KeyBERT.
    
    Parameters:
        text (str): The input document text.
        top_n (int): Number of keywords to return.
        method (str): One of 'default', 'maxsum', or 'mmr'.
        
    Returns:
        List of (keyword, score) tuples.
    """
    if method == 'maxsum':
        keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words='english',
            use_maxsum=True,
            nr_candidates=20,
            top_n=top_n
        )
    elif method == 'mmr':
        keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words='english',
            use_mmr=True,
            diversity=0.7,
            top_n=top_n
        )
    else:
        keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words='english',
            top_n=top_n
        )
    
    return keywords
