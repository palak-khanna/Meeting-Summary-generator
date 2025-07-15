# 🎙️ AI-Powered Meeting Summarizer & Assistant

An intelligent end-to-end system that transcribes meeting audio, generates structured minutes of meeting (MoM), provides a downloadable PDF, and allows contextual Q&A using a memory-augmented chatbot.

---

## 🚀 Features

✅ Whisper-based transcription (offline)  
✅ Automatic speaker tagging (Speaker 1 / 2)  
✅ OpenAI GPT-powered summarization + MOM generation  
✅ PDF export with structured content  
✅ Chatbot with RAG + persistent memory  
✅ Vector database using FAISS for meeting indexing  
✅ Session memory with chat history  
✅ Dynamic UI with multiple meetings and download options  

---

## 🧱 Tech Stack

| Tool | Use |
|------|-----|
| `Streamlit` | Frontend Web App |
| `Whisper` | Audio transcription |
| `OpenAI GPT-3.5` | Summarization, Chat Q&A |
| `FAISS` | Vector-based retrieval |
| `LangChain` | Memory, RAG orchestration |
| `FPDF` | MoM PDF generation |
| `Python` | Core scripting |
| `dotenv` | Environment management |

---

## 🧩 Folder Structure
```bash
MeetingSummarizer/
│
├── app.py # Main Streamlit application
├── requirements.txt
├── .env # Contains your OpenAI API key
│
├── data/ # Stores audio, transcripts, PDFs
│ └── meeting1.mp3
│ └── meeting1_transcript.txt
│ └── meeting1_MOM.pdf
│
├── db/
│ ├── index.json # Meeting index list
│ ├── chat_history/ # JSONs storing persistent Q&A
│ └── faiss_index/ # FAISS vectorstore per meeting
│ └── meeting1/
│ └── index.faiss
│ └── index.pkl
│
├── utils/
│ ├── whisper_transcriber.py # Transcription logic
│ ├── gpt_summarizer.py # Summarization using GPT
│ ├── pdf_generator.py # MOM PDF generation
│ ├── langchain_rag.py # FAISS + LangChain RAG
│ └── memory_handler.py # Persistent memory utils

```

---

## 🔧 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/meeting-summarizer.git
cd meeting-summarizer
```
### 2. (Optional) Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Whisper and audio processing needs it.

Download from: https://ffmpeg.org/download.html

Extract and add ffmpeg/bin to your system PATH

Confirm with: ffmpeg -version

### 5. Set Up .env
Create a file named .env in root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
### 6.▶️ Running the App
```bash
streamlit run app.py
```
