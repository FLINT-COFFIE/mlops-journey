# Write your solution here
year = int(input("Year: "))
leap = year
# conditionals
while True:
    year += 1

    if year % 400 == 0:
        print(f"The next leap year after {leap} is {year}")
        break

    if year % 100 == 0:
        year += 1

    elif year % 4 == 0:
        print(f"The next leap year after {leap} is {year}")
        break
