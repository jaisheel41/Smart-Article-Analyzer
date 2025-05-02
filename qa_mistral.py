# qa_flan.py

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_paragraph_answer(question, context):
    prompt = f"Answer the following question using this context:\n\nContext:\n{context}\n\nQuestion: {question}"
    response = generator(prompt, max_new_tokens=300)[0]['generated_text']
    return response.strip()
