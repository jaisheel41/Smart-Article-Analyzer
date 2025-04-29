# preprocess.py

import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Download stopwords if not already done
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_words(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

def lemmatize_tokens(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc if token.lemma_ != '-PRON-']

def preprocess(text, do_lemmatize=True):
    cleaned = clean_text(text)
    tokens = tokenize_words(cleaned)
    tokens = remove_stopwords(tokens)
    if do_lemmatize:
        tokens = lemmatize_tokens(tokens)
    return tokens

def tokenize_sentences(text):
    return sent_tokenize(text)
