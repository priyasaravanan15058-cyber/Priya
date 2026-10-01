from qna import answer_question


def create_study_plan(topic):
    prompt = f"""
Create a practical 7-day study plan for the topic below.

Topic: {topic}

For each day include:

- What to learn
- A small practice task
- A quick self-check question

Keep it suitable for a student.
"""

    return answer_question(prompt)