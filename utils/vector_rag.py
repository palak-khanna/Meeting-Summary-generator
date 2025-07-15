from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class MeetingRAG:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.index = None
        self.docs = []

    def add_document(self, text):
        self.docs.append(text)
        vectors = self.vectorizer.fit_transform(self.docs).toarray()
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(np.array(vectors).astype('float32'))

    def query(self, q):
        vec = self.vectorizer.transform([q]).toarray().astype('float32')
        D, I = self.index.search(vec, k=1)
        return self.docs[I[0][0]] if I[0][0] < len(self.docs) else ""

    def ask_question(self, question):
        context = self.query(question)
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You're a helpful meeting assistant. Use the provided context to answer."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
            ],
            temperature=0.4
        )
        return response.choices[0].message.content
