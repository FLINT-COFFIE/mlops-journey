# write your solution here
# taking the file inputs
student_info = input("Enter student info file name: ")
exercise_info = input("Enter exercise info file name: ")
exam_info = input("Enter exam file name: ")

student = {}
exercise = {}
exam = {}

# student info
with open(student_info) as f:
    # loop through line and split
    for line in f:
        # strip before you split
        parts = line.strip()
        parts = parts.split(";")

        # define variables
        id = parts[0]
        name = f"{parts[1]} {parts[2]}"

        # if header continue
        if id == "id":
            continue

        # add student
        student[id] = name

# exercise info
with open(exercise_info) as f:
    for line in f:
        parts = line.strip()
        parts = parts.split(";")

        id = parts[0]
        exercises = parts[1:]

        # if header continue
        if id == "id":
            continue

        sum_exercises = 0
        for num in exercises:
            sum_exercises += int(num)

        exercise[id] = sum_exercises

# exam info
with open(exam_info) as f:
    # loop through line and split
    for line in f:
        # strip before you split
        parts = line.strip()
        parts = parts.split(";")

        # define variables
        id = parts[0]
        exam_points = parts[1:]

        # if header continue
        if id == "id":
            continue

        # add points
        sum_exams = 0
        for num in exam_points:
            sum_exams += int(num)

        exam[id] = sum_exams

for id, name in student.items():
    if id in exam:
        exam_p = exam[id]
        identity = name
        exercise_p = exercise[id] // 4

        total_points = exam_p + exercise_p

        if total_points > 0 and total_points <= 14:
            grade = 0
        elif total_points > 14 and total_points <= 17:
            grade = 1
        elif total_points > 17 and total_points <= 20:
            grade = 2
        elif total_points > 20 and total_points <= 23:
            grade = 3
        elif total_points > 23 and total_points <= 27:
            grade = 4
        elif total_points > 27:
            grade = 5

        print(f"{name} {grade}")
