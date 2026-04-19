class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    accepted = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    return accepted

def attempts_with_grade(attempts: list, grade: int):
    target = list(filter(lambda attempt: attempt.grade == grade, attempts))
    return target
    
def passed_students(attempts: list, course: str):
    passed = filter(lambda attempt: attempt.grade >= 1 and attempt.course_name == course, attempts)
    #passed_course = list(filter(lambda attempt: attempt.course_name == course, passed))
    return sorted(list(map(lambda a : a.student_name, passed)))


if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)