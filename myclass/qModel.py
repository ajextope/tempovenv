from operator import rshift
import myclass.dbConnection as db
class Questions():
    def __init__(self,question: str, correct_answer: str, choices: list):
        self.question_item = question
        self.correct_answer = correct_answer
        self.choices = choices


