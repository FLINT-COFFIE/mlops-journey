# Write your solution here
# functions
def results(scores):
    # separate exams and exercises
    # space = scores.find(" ")
    space = scores.split()
    exam = int(space[0])
    exercise = int(space[1])
    if 0 <= exam <= 20 and 0 <= exam <= 100:
        return exam, exercise


# def pass_percentage(exam, exercise):
#   print(f"Points average: {}")


def points(exam, exercise):
    # exercise points
    total_points = 0
    if exam < 10:
        total_points = 0

    else:
        exercise_points = exercise // 10
        # total points
        total_points = exercise_points + exam

    return total_points


def grade(total_points):
    if 0 <= total_points <= 14:
        return 0
    if 15 <= total_points <= 17:
        return 1
    if 18 <= total_points <= 20:
        return 2
    if 21 <= total_points <= 23:
        return 3
    if 24 <= total_points <= 27:
        return 4
    if 28 <= total_points <= 30:
        return 5


while True:
    scores = input("Exam points and exercises completed: ")
    if scores == "":
        print(grade(points(results(scores))))
