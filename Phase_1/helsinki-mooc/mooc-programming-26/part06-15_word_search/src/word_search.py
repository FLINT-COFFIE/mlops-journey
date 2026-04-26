# Write your solution here
# make a dictionary with the search term as the key and list of words as values
def find_words(search_term: str):
    results = []
    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            # if wildcards
            # if searchterm startswith *
            if search_term.startswith("*"):
                word = search_term[1:]
                if line.endswith(word):
                    results.append(line)

            # if searchterm endswith *
            elif search_term.endswith("*"):
                word = search_term[:-1]
                if line.startswith(word):
                    results.append(line)

            # dots
            elif "." in search_term:
                if len(line) == len(search_term):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and line[i] != search_term[i]:
                            match = False
                            break
                    if match:
                        results.append(line)

            # returning match if no wildcards
            elif search_term.lower() == line:
                results.append(line)
    return results


if __name__ == "__main__":
    print(find_words("*vokes"))
