from difficulty import Difficulty
from question import Question


class QuestionStore:

    def __init__(self):
        self.questions = [
            Question('Q1', Difficulty.EASY, 1),
            Question('Q2', Difficulty.EASY, 2),
            Question('Q3', Difficulty.MEDIUM, 2),
            Question('Q4', Difficulty.HARD, 9),
            Question('Q5', Difficulty.EASY, 3),
            Question('Q6', Difficulty.HARD, 7),
            Question('Q7', Difficulty.MEDIUM, 3),
            Question('Q8', Difficulty.EASY, 3),
            Question('Q9', Difficulty.MEDIUM, 5),
            Question('Q10', Difficulty.HARD, 5)
        ]
