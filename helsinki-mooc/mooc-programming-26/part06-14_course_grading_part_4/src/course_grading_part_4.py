# tee ratkaisu tänne
# tee ratkaisu tänne
# write your solution here
# taking the file inputs
student_info = "students2.csv"  # input("Enter student info file name: ")
exercise_info = "exercises2.csv"  # input("Enter exercise info file name: ")
exam_info = "exam_points2.csv"  # input("Enter exam file name: ")
course_info = "course2.txt"  # input("Enter course file: ")


student = {}
exercise = {}
exam = {}
course = {}


# course info
def courses(filename: str):
    with open(filename) as file:
        for line in file:
            line = line.split(":")
            course_list = []
            for item in line:
                item = item.strip()
                course_list.append(item)
            course[course_list[0]] = course_list[1]


courses(course_info)

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


print(
    f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}"
)

with open("results.csv", "w") as file:
    pass
with open("results.txt", "w") as file:
    pass

for id, name in student.items():
    if id in exam:
        exam_p = exam[id]
        identity = name
        exercise_p = exercise[id] // 4

        total_points = exam_p + exercise_p

        if total_points >= 0 and total_points <= 14:
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

        with open("results.txt", "w") as file:
            first_line = f"{course['name']}, {course['study credits']} credits\n"
            file.write(first_line)
            file.write(f"{'=' * len(first_line)}\n")
            student_line = f"{name:<30}{exercise[id]:<10}{exercise_p:<10}{exam_p:<10}{total_points:<10}{grade:<10}"
            file.write(student_line)

        with open("results.csv", "a") as f:
            f.write(f"{id};{name};{grade}\n")

# write a func to read the course info
# print a ======= line
#
