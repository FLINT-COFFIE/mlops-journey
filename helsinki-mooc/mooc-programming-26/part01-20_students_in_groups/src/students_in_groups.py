# Write your solution here
#inputs
students = int(input("How many students: "))
size = int(input("Desired group size: "))

groups = (students + size -1) // size
print(f"Number of groups formed: {groups}")
