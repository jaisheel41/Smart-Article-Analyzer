# summarizer.py

from transformers import pipeline
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_into_chunks(text, max_chunk_size=1024):
    """
    Split long text into manageable chunks based on sentence boundaries.
    """
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def abstractive_summary(text, max_len=150):
    """
    Generate an abstractive summary using a transformer model.
    Handles long documents by chunking.
    """
    text_chunks = split_into_chunks(text)
    summaries = []

    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=max_len, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return summaries
