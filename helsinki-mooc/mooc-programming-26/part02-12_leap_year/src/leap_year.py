# Write your solution here
year = int(input("Year: "))

# conditionals
if year % 400 == 0:
    print("That year is a leap year.")

elif year % 100 == 0:
    print("That year is not a leap year.")

elif year % 4 == 0:
    print("That year is a leap year.")

else:
    print("That year is not a leap year.")
