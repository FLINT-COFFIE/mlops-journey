# Write your solution here
age = int(input("What is your age? "))

if 5 <= age <= 90:
    print(f"Ok, you're {age} years old")

elif 0 <= age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
