# utils.py

import os

def save_to_file(content, filename, folder="outputs"):
    """
    Save given content (string or list) to a text file.
    Automatically creates the folder if it doesn't exist.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if isinstance(content, list):
        content = "\n".join(content)
    
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Saved output to: {filepath}")

def print_list(title, items):
    """
    Nicely print a list with a title.
    """
    print(f"\n--- {title} ---")
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item}")
