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
    students[student].append(courses)


students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")
