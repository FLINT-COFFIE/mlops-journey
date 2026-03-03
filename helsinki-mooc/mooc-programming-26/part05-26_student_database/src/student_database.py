# Write your solution here
# PART 1
def add_student(students: dict, student: str):
    students[student] = []


def print_student(students: dict, student: str):
    if student not in students:
        print(f"{student}: no such person in the database")

    else:
        if len(students[student]) < 1:
            print(f"{student}:")
            print("no completed courses")

        # PART 2

        else:
            print(f"{student}:")
            print(f" {len(students[student])} completed courses:")

            total = 0
            for course in students[student]:
                print(f"  {course[0]} {course[1]}")

                total += course[1]
            average_grade = total / len(students[student])

            print(f" average grade {average_grade}")


def add_course(students: dict, student: str, courses: tuple):
    course_name, grade = courses
    found = False
    if grade > 0:
        for i in range(len(students[student])):
            if students[student][i][0] == course_name:
                found = True
                if grade > students[student][i][1]:
                    students[student][i] = courses
                break

        if found == False:
            students[student].append(courses)


def summary(students: dict):
    count = 0
    highest = ()
    # avg = total grade / len(courses)
    best_avg = 0

    for key, values in students.items():
        if len(values) > count:
            highest = len(values), key
            count = len(values)

        for student in students:
            grade = 0

            # name = ""
            for i in range(len(values)):
                grade += values[i][1]
            avg = grade / len(values)

            if avg > best_avg:
                best_avg = avg
                name += student

    print(f"students {len(students)}")
    print(f"most courses completed {highest[0]} {highest[1]}")
    print(f"best average grade {best_avg} {student}")
    print(students)


students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)
