# Write your solution here
# read and return dictionary
def filter_incorrect():
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            line = line.split(";")

            week = line[0]
            numbers_str = line[1]

            week_str = week.split(" ")
            if week_str[0] != "week":
                continue

            week_int = week_str[1]

            try:
                week_int = int(week_int)

            except ValueError:
                continue

            numbers_str = numbers_str.split(",")

            if len(numbers_str) != 7:
                continue

            correct = []

            bad = False

            for num in numbers_str:
                try:
                    num = int(num)

                    if num < 1 or num > 39:
                        bad = True

                        break

                    if num in correct:
                        bad = True

                        break

                    else:
                        correct.append(num)

                except ValueError:
                    bad = True
                    break

                if not bad and len(correct) == 7:
                    with open("correct_numbers.csv", w) as right:
                        right.write(line + "\n")


if __name__ == "__main__":
    filter_incorrect()
