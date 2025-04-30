# main.py

from extract_text import extract_text
from preprocess import preprocess
from summarizer import abstractive_summary
from keywords import extract_keywords
#from qa_basic import answer_question
from qa_advanced import answer_question
from memory_store import load_memory, save_summary, save_keywords, save_qa, display_memory
from utils import save_to_file, print_list

import os
from memory_store import (
    load_memory,
    save_summary,
    save_keywords,
    save_qa,
    display_memory
)


def main():
    print("📚 Smart Article Analyzer\n")

    file_path = input("Enter the file path (PDF, TXT, or DOCX): ").strip()

    try:
        file_id = os.path.splitext(os.path.basename(file_path))[0]

        # Load existing memory and show it
        memory = load_memory(file_id)
        display_memory(memory)

        # Extract new text
        raw_text = extract_text(file_path)
        print(f"\n✅ Text extracted successfully. Total characters: {len(raw_text)}")

        tokens = preprocess(raw_text, do_lemmatize=False)
        print(f"✅ Preprocessing done. Total tokens: {len(tokens)}")

        # === SUMMARY ===
        summary_sentences = abstractive_summary(raw_text, max_len=130)
        print_list("Summary", summary_sentences)
        save_to_file(summary_sentences, "summary.txt")
        save_summary(file_id, summary_sentences)

        # === KEYWORDS ===
        #keywords = extract_keywords(raw_text, top_n=10)
        keywords = extract_keywords(raw_text, top_n=10, method='mmr')
        keywords_formatted = [f"{word} ({score:.4f})" for word, score in keywords]
        print_list("Top Keywords", keywords_formatted)
        save_to_file(keywords_formatted, "keywords.txt")
        save_keywords(file_id, keywords)

        # === QUESTION ANSWERING ===
        ask_question = input("\n❓ Do you want to ask a question about the document? (yes/no): ").lower()
        if ask_question in ["yes", "y"]:
            question = input("Enter your question: ").strip()
            answer = answer_question(raw_text, question)
            print(f"\nAnswer: {answer}")
            qa_content = f"Q: {question}\nA: {answer}"
            save_to_file(qa_content, "qa_answer.txt")
            save_qa(file_id, question, answer)

        print("\n📁 All outputs saved in the 'outputs' folder.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
