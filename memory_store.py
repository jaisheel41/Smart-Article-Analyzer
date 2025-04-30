# memory_store.py

import os
import json
from datetime import datetime

MEMORY_FOLDER = "outputs/memory/"

def _get_memory_path(file_id):
    if not os.path.exists(MEMORY_FOLDER):
        os.makedirs(MEMORY_FOLDER)
    return os.path.join(MEMORY_FOLDER, f"{file_id}.json")

def load_memory(file_id):
    """
    Load existing memory for a document.
    """
    path = _get_memory_path(file_id)
    if not os.path.exists(path):
        return {"summary": [], "keywords": [], "qa": []}
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_summary(file_id, summary_lines):
    memory = load_memory(file_id)
    memory["summary"] = summary_lines
    _save(file_id, memory)

def save_keywords(file_id, keyword_tuples):
    memory = load_memory(file_id)
    memory["keywords"] = keyword_tuples
    _save(file_id, memory)

def save_qa(file_id, question, answer):
    memory = load_memory(file_id)
    memory["qa"].append({
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().isoformat()
    })
    _save(file_id, memory)

def _save(file_id, data):
    path = _get_memory_path(file_id)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def display_memory(memory):
    print("\n🧠 Loaded Previous Summary:")
    for s in memory["summary"]:
        print(f"- {s}")
    
    print("\n🔑 Previous Keywords:")
    for kw, score in memory["keywords"]:
        print(f"- {kw} ({score:.2f})")
    
    print("\n❓ Past Questions:")
    for qa in memory["qa"]:
        print(f"[{qa['timestamp']}] Q: {qa['question']} \n → A: {qa['answer']}")
