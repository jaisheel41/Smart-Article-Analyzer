# report_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from datetime import datetime

def create_pdf_report(file_id, memory, output_dir="outputs/reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(output_dir, f"{file_id}_report.pdf")
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    margin = 1 * inch
    cursor_y = height - margin

    def draw_title(text, size=16):
        nonlocal cursor_y
        c.setFont("Helvetica-Bold", size)
        c.drawString(margin, cursor_y, text)
        cursor_y -= 20

    def draw_text(text, size=11, spacing=14):
        nonlocal cursor_y
        c.setFont("Helvetica", size)
        lines = text.split("\n")
        for line in lines:
            if cursor_y < margin:
                c.showPage()
                cursor_y = height - margin
            c.drawString(margin, cursor_y, line)
            cursor_y -= spacing

    # Title
    draw_title(f"🧠 Smart Article Report: {file_id}")
    draw_text(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    # Summary
    draw_title("Summary", size=14)
    draw_text("\n".join(memory.get("summary", [])))

    # Keywords
    draw_title("Top Keywords", size=14)
    keywords = memory.get("keywords", [])
    draw_text("\n".join([f"- {kw} ({score:.2f})" for kw, score in keywords]))

    # Q&A
    draw_title("Question & Answer History", size=14)
    for qa in memory.get("qa", []):
        draw_text(f"\nQ: {qa['question']}\nA: {qa['answer']}\n")

    # Save
    c.save()
    print(f"✅ PDF report saved to: {filename}")
