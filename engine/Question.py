import random


class Answer:
    def __init__(self):
        self.style = "List Number 2"
        self.text = ''

    def add_text(self, text):
        self.text = text


class Question:
    def __init__(self):
        self.style = "List Number"
        self.answers = []
        self.text = ''

    def add_answer(self, answer_text):
        answer = Answer()
        answer.add_text(answer_text)
        self.answers.append(answer)

    def shuffle_answer(self):
        random.shuffle(self.answers)

    def reset(self):
        self.answers = []
        self.text = ''
