# Write your solution here
def print_many_times(word_to_print, lines):
    num = 0
    while num < lines:
        print(word_to_print)
        num += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
