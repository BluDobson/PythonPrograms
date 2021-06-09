class Student:
    class_ ="student"
    def __init__(self, name, age, score1, score2, score3):
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    
    def avg_score(self):
        return int(self.score1 + self.score2 + self.score3)/3

Entry = Student(input("Enter your name here: "), input("Enter your age here: "), int(input("Enter the first test score: ")), int(input("Enter the first second score: ")), int(input("Enter the first third score: ")))
print(Entry.avg_score())
