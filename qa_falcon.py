# qa_falcon.py

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_paragraph_answer(question, context):
    prompt = f"""
Context:
{context}

Question: {question}

Answer this question in a detailed paragraph, using the context above.
"""
    output = generator(prompt, max_new_tokens=300, temperature=0.7, do_sample=True)[0]['generated_text']
    return output.split("Answer this question in a detailed paragraph, using the context above.")[-1].strip()
