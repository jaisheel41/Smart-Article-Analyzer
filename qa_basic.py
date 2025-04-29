# qa_basic.py

from transformers import pipeline

# Load Question-Answering pipeline (will download model automatically)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(context_text, question):
    """
    Answer a question given the context text.
    Returns the answer string.
    """

    if not context_text.strip():
        return "Context is empty."

    if not question.strip():
        return "Question is empty."

    result = qa_pipeline({
        "context": context_text,
        "question": question
    })

    return result['answer']
