from pypdf import PdfReader

# ---------------------------
# PDF Extraction
# ---------------------------
def extract_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text

# ---------------------------
# Chunking Function
# ---------------------------
def split_text(text, chunk_size=1500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# ---------------------------
# INPUT
# ---------------------------
choice = input("1. Enter text\n2. Use PDF\nEnter choice: ")

if choice == "1":
    text = input("Enter text:\n")
else:
    file_path = input("Enter PDF file path: ")
    text = extract_pdf(file_path)

# ---------------------------
# CHUNKING
# ---------------------------
chunks = split_text(text)

print(f"\nTotal chunks created: {len(chunks)}")

# ---------------------------
# SAVE TO FILE
# ---------------------------
with open("chunks.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"\n\n===== CHUNK {i+1} =====\n")
        f.write(chunk)

print(" Chunks saved in chunks.txt")