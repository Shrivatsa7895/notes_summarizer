# AI Lecture Notes Summarizer

## Project Overview
The AI Lecture Notes Summarizer is a Python-based application that automatically converts long lecture notes and PDF documents into concise, easy-to-understand summaries using Natural Language Processing (NLP) and AI.

It helps students save time by extracting important information from lengthy study materials.

## Features
- Accepts text input and PDF documents.
- Extracts text from uploaded PDF files.
- Splits long documents into smaller chunks.
- Generates summaries using a pretrained Hugging Face Transformer model.
- Combines summarized content into readable notes.
- Provides a simple Streamlit user interface.

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- PyPDF
- PyTorch

## Project Structure

```text
notes_summarizer/
│
├── app.py
├── main.py
├── chunk.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shrivatsa7895/notes_summarizer.git
```

### 2. Navigate to the Project Folder

```bash
cd notes_summarizer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

To start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to use the application.

## How It Works

1. Enter lecture text or upload a PDF document.
2. The application extracts the text from the document.
3. Long text is divided into smaller chunks.
4. Each chunk is processed using a pretrained Transformer model.
5. The generated summaries are combined into concise lecture notes.
6. View and use the summarized content.

## Future Improvements
- Generate topic-wise summaries.
- Support multiple document formats.
- Add keyword extraction.
- Improve summary accuracy and readability.
- Support multiple languages.

## Author
Developed as an Artificial Intelligence and Machine Learning academic project.
