# write your solution here
# taking the file inputs
student_info = input("Enter student info file name: ")
exercise_info = input("Enter exercise info file name: ")

student = {}
exercise = {}


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

for id, name in student.items():
    if id in exercise:
        ex = exercise[id]
        print(f"{name} {ex}")

# part 1 completed
