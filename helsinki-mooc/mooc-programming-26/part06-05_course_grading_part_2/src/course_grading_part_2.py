# write your solution here
# taking the file inputs
student_info = input("Enter student info file name: ")
exercise_info = input("Enter exercise info file name: ")
exam_info = input("Enter exam file name: ")

student = {}
exercise = {}
exam_info = {}

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
with open(exam_info) as f:
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
        exam_points = parts[1]

        # if header continue
        if id == "id":
            continue

        # add points
        sum_exams = 0
        for num in exam_points:
            sum_exams += int(num)

        exam_info[id] = sum_exams
