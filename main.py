from flask import Flask, render_template, request, jsonify

from qna import answer_question
from explanation import explain_topic
from summary_module import summarize_topic
from learning_path import create_study_plan


app = Flask(__name__, template_folder="Templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask():

    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()
    request_type = data.get("type", "ask").strip().lower()

    if not question:
        return jsonify({
            "answer": "Please enter a question or topic."
        }), 400

    if request_type == "explain":

        answer = explain_topic(question)

    elif request_type == "summarize":

        answer = summarize_topic(question)

    elif request_type == "study":

        answer = create_study_plan(question)

    elif request_type == "quiz":

        prompt = f"""
Create a short quiz on this topic for a student.

Topic: {question}

Create 5 multiple-choice questions.

For each question:
- Give 4 options (A-D)
- Do not reveal the answer immediately

After all questions, give an Answer Key with:
- Correct option
- One-line explanation
"""

        answer = answer_question(prompt)

    else:

        answer = answer_question(question)

    return jsonify({
        "answer": answer
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )