# Write your solution here
# letters
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first < second < third:
    print(f"The letter in the middle is {second}")

elif third < second < first:
    print(f"The letter in the middle is {second}")

elif second < first < third:
    print(f"The letter in the middle is {first}")

elif third < first < second:
    print(f"The letter in the middle is {first}")

elif second < third < first:
    print(f"The letter in the middle is {third}")

elif first < third < second:
    print(f"The letter in the middle is {third}")
