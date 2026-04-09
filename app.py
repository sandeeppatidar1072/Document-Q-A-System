from flask import Flask, render_template, request
from utils import extract_text, process_text, get_answer

app = Flask(__name__)

# Global storage
chunks = []
vectorizer = None
vectors = None


@app.route("/", methods=["GET", "POST"])
def index():
    global chunks, vectorizer, vectors
    answer = ""

    if request.method == "POST":

        # Upload PDF
        if "pdf" in request.files and request.files["pdf"].filename != "":
            file = request.files["pdf"]
            text = extract_text(file)
            chunks, vectorizer, vectors = process_text(text)
            answer = "✅ PDF uploaded successfully! Now ask a question."

        # Ask question
        elif "question" in request.form and chunks:
            question = request.form["question"]
            answer = get_answer(question, chunks, vectorizer, vectors)

        else:
            answer = "⚠️ Please upload a PDF first."

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)