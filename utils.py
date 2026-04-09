import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


def process_text(text):
    # Split into chunks (simple lines)
    chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunks)

    return chunks, vectorizer, vectors


def get_answer(question, chunks, vectorizer, vectors):
    q_vector = vectorizer.transform([question])
    similarity = cosine_similarity(q_vector, vectors)

    index = similarity.argmax()
    return chunks[index]