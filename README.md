# 📚 Smart Article Analyzer

Smart Article Analyzer is a fully local, open-source AI tool that helps you understand, explore, and interact with any document — offline, intelligently, and with memory. Upload a PDF, DOCX, or TXT file and get a clean summary, keyword insights, detailed answers to your questions, and a full report — all without needing an internet connection or API keys.

---

## 🧠 Features

- ✅ Upload and analyze **PDF, DOCX, or TXT** documents
- ✨ Get an **abstractive summary** using `PEGASUS`
- 🔑 Extract **semantic keywords** with `KeyBERT + mpnet`
- ❓ Ask **unlimited questions** with detailed, paragraph-style answers
- 💾 Persistent **file memory**: stores summary, keywords, and Q&A history
- 📄 Export a full **PDF report** from any session
- 🔁 Works **100% offline** — no OpenAI, no API keys, no data sharing

---

## ⚙️ Tech Stack

| Component          | Tool / Model                         |
|--------------------|--------------------------------------|
| Summarization       | `google/pegasus-xsum`                |
| Question Answering  | `flan-t5-base`, `zephyr-7b-beta`, or `mistral-7b-instruct` (optional, switchable) |
| Keyword Extraction  | `KeyBERT` with `all-mpnet-base-v2`  |
| PDF Parsing         | `PyMuPDF`, `python-docx`             |
| Report Generation   | `reportlab`                          |
| File Memory         | JSON per document                   |
