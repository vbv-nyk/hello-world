# Pure Python data processing
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average = sum(scores) / len(scores)

class Processor:
    def __init__(self, data):
        self.students = [Student(d["name"], d["scores"]) for d in data]

    def top_student(self):
        return max(self.students, key=lambda s: s.average)

    def class_average(self):
        total = sum(s.average for s in self.students)
        return total / len(self.students)
