from difficulty import Difficulty


class Question:
    def __init__(self, id: str, difficulty: Difficulty, marks: int):
        self.id = id
        self.difficulty = difficulty
        self.marks = marks

    def __repr__(self):
        return "{} {} {}".format(self.id, self.difficulty, self.marks)