from transformers import pipeline
from pypdf import PdfReader
import os
import warnings
import re

warnings.filterwarnings("ignore")

# ---------------------------
# Load Model (FASTER MODEL)
# ---------------------------
print("Loading model...")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
print("Model loaded!")

# ---------------------------
# PDF Extraction
# ---------------------------
def extract_pdf(file_path):
    if not os.path.exists(file_path):
        print(" File not found!")
        return ""

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text

# ---------------------------
# Clean Text
# ---------------------------
def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("- ", "")
    text = " ".join(text.split())
    return text

# ---------------------------
# Chunking
# ---------------------------
def split_text(text, chunk_size=400):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]

        if "." in chunk:
            chunk = chunk[:chunk.rfind(".") + 1]

        chunks.append(chunk)

    return chunks

# ---------------------------
# Input
# ---------------------------
print("\nChoose input method:")
print("1. Enter text manually")
print("2. Use PDF file")

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    text = input("\nEnter your lecture text:\n")

elif choice == "2":
    file_path = input("\nEnter PDF file path: ").strip().strip('"')
    text = extract_pdf(file_path)

    if text == "":
        print(" No text extracted.")
        exit()

    text = clean_text(text)

else:
    print(" Invalid choice")
    exit()

# ---------------------------
# Processing
# ---------------------------
chunks = split_text(text)

summaries = []

for chunk in chunks:
    if len(chunk.strip()) < 30:
        continue

    word_count = len(chunk.split())

    max_len = min(60, max(10, word_count // 2))
    min_len = max(5, max_len // 2)

    result = summarizer(
        chunk,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    summaries.append(result[0]['summary_text'])

# ---------------------------
# Output
# ---------------------------
print("\n" + "="*40)
print(" AUTOMATIC LECTURE NOTES")
print("="*40 + "\n")

final_notes = []
seen = set()

for s in summaries:
    points = re.split(r'\.|\n', s)

    for p in points:
        p = p.strip()

        if len(p) > 10 and p not in seen:
            note = "• " + p
            print(note)
            final_notes.append(note)
            seen.add(p)

# ---------------------------
# Save
# ---------------------------
with open("notes.txt", "w", encoding="utf-8") as f:
    for note in final_notes:
        f.write(note + "\n")

print("\n Notes saved to notes.txt")