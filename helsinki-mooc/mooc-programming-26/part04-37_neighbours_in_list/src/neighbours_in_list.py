# Write your solution here
def longest_series_of_neighbours(num_list):
    # 1 because the streak cannot be zero
    longest = 1
    current = 1
    #
    for i in range(len(num_list) - 1):
        if abs(num_list[i] - num_list[i + 1]) == 1:
            current += 1

        else:
            # reset current
            current = 1

        # increase longest
        if current > longest:
            longest = current

    return longest


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
