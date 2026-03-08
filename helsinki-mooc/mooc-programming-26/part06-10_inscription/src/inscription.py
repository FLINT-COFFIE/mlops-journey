# Write your solution here
sign = input("Whom should I sign this to: ")
directory = input("Where shall I save it: ")

with open(directory, "w") as my_file:
    my_file.write(
        f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
    )
