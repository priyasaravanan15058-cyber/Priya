from qna import answer_question


def explain_topic(topic):
    prompt = f"""
Explain the following topic to a student in simple words.

Topic: {topic}

Include:

1. Simple definition
2. How it works
3. One real-world example
4. Key points
"""

    return answer_question(prompt)