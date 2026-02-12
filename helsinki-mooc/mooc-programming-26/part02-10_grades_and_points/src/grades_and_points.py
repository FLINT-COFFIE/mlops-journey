# Write your solution here
points = int(input("Enter amount of points received: "))

# conditionals
if points < 0:
    print("impossible!")

elif points < 50:
    print("fail")

elif points < 60:
    print("Grade: 1")

elif points < 70:
    print("Grade: 2")

elif points < 80:
    print("Grade: 3")

elif points < 90:
    print("Grade: 4")

elif points < 101:
    print("Grade: 5")

elif points > 100:
    print("impossible!")
