# main.py

from extract_text import extract_text
from preprocess import preprocess
from summarizer import abstractive_summary
from keywords import extract_keywords
#from qa_basic import answer_question
from qa_advanced import answer_question
from memory_store import load_memory, save_summary, save_keywords, save_qa, display_memory
from utils import save_to_file, print_list
from report_generator import create_pdf_report
from qa_falcon import generate_paragraph_answer
from qa_advanced import get_top_k_chunks, split_text_to_chunks


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
        while True:
            ask = input("\n❓ Ask a question about the document (or type 'exit' to stop): ").strip()
            if ask.lower() == 'exit':
                break
            top_chunks = get_top_k_chunks(ask, split_text_to_chunks(raw_text))
            context = top_chunks[0]
            answer = generate_paragraph_answer(ask, context)
            print(f"\n📘 Answer:\n{answer}")
            save_to_file(f"Q: {ask}\nA: {answer}", "qa_answer.txt")
            save_qa(file_id, ask, answer)


    except Exception as e:
        print(f"❌ Error: {e}")

    
    create_pdf_report(file_id, load_memory(file_id))


if __name__ == "__main__":
    main()
