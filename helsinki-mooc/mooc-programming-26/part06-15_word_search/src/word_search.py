# Write your solution here
# make a dictionary with the search term as the key and list of words as values
def find_words(search_term: str):
    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            if search_term.lower() in line:
                print(line)


find_words("vokes")
