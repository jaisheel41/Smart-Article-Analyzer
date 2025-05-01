# summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def abstractive_summary(text, max_len=160):
    # Pegasus prefers short inputs; chunk if needed
    if len(text) > 1000:
        text = text[:1000]
    result = summarizer(text, max_length=max_len, min_length=60, do_sample=False)
    return [result[0]['summary_text']]
