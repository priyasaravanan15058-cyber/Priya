from qna import answer_question


def summarize_topic(topic):
    prompt = f"""
Summarize the following topic for a student.

Topic: {topic}

Give:

- A short summary
- 5 key points
- Important terms
"""

    return answer_question(prompt)