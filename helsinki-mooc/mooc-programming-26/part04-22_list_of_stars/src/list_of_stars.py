# Write your solution here
def list_of_stars(int_list):
    for char in int_list:
        print("*" * char)


if __name__ == "__main__":
    int_list = [3, 7, 1, 1, 2]
    list_of_stars(int_list)
