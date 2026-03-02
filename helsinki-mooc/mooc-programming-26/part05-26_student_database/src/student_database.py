# Write your solution here
def add_student(students: dict, student: str):
    students[student] = []


def print_student(students: dict, student: str):
    if student not in students:
        print(f"{student}: no such person in the database")

    else:
        if len(students[student]) < 1:
            print(f"{student}:")
            print("no completed courses")


students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")
