# qa_advanced.py

from sentence_transformers import SentenceTransformer
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download("punkt")
from nltk.tokenize import sent_tokenize

# Load embedding model and QA pipeline
embedder = SentenceTransformer("all-MiniLM-L6-v2")
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def split_text_to_chunks(text, max_sentences=5):
    """
    Split text into chunks of N sentences each for retrieval.
    """
    sentences = sent_tokenize(text)
    chunks = [
        " ".join(sentences[i:i + max_sentences])
        for i in range(0, len(sentences), max_sentences)
    ]
    return chunks

def get_top_k_chunks(question, chunks, k=3):
    """
    Use semantic similarity to find top-k relevant chunks for the question.
    """
    question_embedding = embedder.encode([question])
    chunk_embeddings = embedder.encode(chunks)

    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]
    top_k_indices = similarities.argsort()[-k:][::-1]
    return [chunks[i] for i in top_k_indices]

def answer_question(text, question, top_k=3):
    """
    Perform context-aware QA using top-K chunk retrieval.
    """
    chunks = split_text_to_chunks(text)
    top_chunks = get_top_k_chunks(question, chunks, k=top_k)

    # Use top-1 chunk for now (best result)
    best_chunk = top_chunks[0]
    result = qa_model(question=question, context=best_chunk)

    return result['answer']
