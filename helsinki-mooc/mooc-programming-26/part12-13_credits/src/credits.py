from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    sum_credits = reduce(lambda credits, item: credits + item.credits, attempts, 0)
    return sum_credits

def sum_of_passed_credits(attempts: list):
    passed = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    sum_credits = reduce(lambda credits, item: credits + item.credits, passed, 0)
    return sum_credits
    
    
def average(attempts: list):
    passed = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    grades = reduce(lambda credits, item: credits + item.grade, attempts, 0)
    return grades / len(passed)


if __name__ == "__main__":
    #testing
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)