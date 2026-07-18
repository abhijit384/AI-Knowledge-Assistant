# 🤖 AI Knowledge Assistant

An AI-powered Knowledge Assistant built using **LangChain**, **Mistral AI**, **ChromaDB**, and **Streamlit**. It uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded documents and websites.

---

## 🚀 Features

- 📄 Upload PDF, DOCX, and TXT documents
- 🌐 Index website content
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered question answering with Mistral AI
- 📚 Displays retrieved source documents
- ⚡ Fast and interactive Streamlit interface
- 🔄 Supports rebuilding the knowledge base

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- ChromaDB
- BeautifulSoup
- PyPDF
- python-docx
- Sentence Transformers

---

## 📂 Project Structure

```text
AI-Knowledge-Assistant/
│
├── app.py
├── rag.py
├── build_db.py
├── loaders.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/abhijit384/AI-Knowledge-Assistant.git
```

Go to the project directory:

```bash
cd AI-Knowledge-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Mistral API key:

```text
MISTRAL_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload documents or enter website URLs.
2. Documents are split into smaller chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User questions retrieve the most relevant chunks.
6. Mistral AI generates answers using only the retrieved context.

---

## 📈 Future Improvements

- Chat history
- Multiple website support
- Document preview
- AI document summarization
- Quiz generation
- Flashcards
- Voice input
- Text-to-speech
- Download chat
- OCR support
- Better UI/UX

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abhijit Bhattacharjya**

GitHub: https://github.com/abhijit384