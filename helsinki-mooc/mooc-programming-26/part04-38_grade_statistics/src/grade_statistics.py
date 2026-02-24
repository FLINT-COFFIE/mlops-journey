# Write your solution here
# functions
def results(scores: int):
    # separate exams and exercises
    # space = scores.find(" ")
    space = scores.split()
    exam = int(space[0])
    exercise = int(space[1])
    if 0 <= exam <= 20 and 0 <= exam <= 100:
        return exam, exercise


# def pass_percentage(exam, exercise):
#   print(f"Points average: {}")


# defining points
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


# defining grade
def grade(total_points: float):
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


# exam in list
exam_list = []
exer_list = []
grad = []
add = []
# count
count = 1

# main code block
while True:
    # take input
    scores = input("Exam points and exercises completed: ")

    # final printout
    if scores == "":
        print("Statistics:")

        # finding avg
        avg = (sum(exam_list) + sum(exer_list)) / len(exam_list)
        pass_perc = (len(add) / len(exam_list)) * 100

        # displaying the values
        print(f"Points average: {avg:.1f}")
        print(f"Pass percentage: {pass_perc:.1f}")
        print("Grade distribution:")

        for i in range(5, -1, -1):
            stars = grad.count(i)

            print(f"{i}: {stars * '*'}")

        break

    # count increment
    exam_toadd, exer_toadd = results(scores)
    exam_list.append(exam_toadd)
    exer_list.append(exer_toadd // 10)

    # all points
    all_points = grade(points(exam_toadd, exer_toadd))

    # setting conditionals
    if exam_toadd < 10:
        final = 0
    else:
        final = all_points
    grad.append(final)

    if final > 0:
        add.append(final)

    # count increment
    count += 1
