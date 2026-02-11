# Write your solution here
print("Person 1:")
Person1 = input("Name: ")
age1 = int(input("Age: "))

print("Person 2:")
Person2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {Person1}")
elif age2 > age1:
    print(f"The elder is {Person2}")
else:
    print(f"{Person1} and {Person2}  are the same age")
