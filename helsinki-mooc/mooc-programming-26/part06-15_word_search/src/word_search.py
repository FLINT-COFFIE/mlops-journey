# Write your solution here
# make a dictionary with the search term as the key and list of words as values
def find_words(search_term: str):
    results = []
    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            
            
                
            #
            elif search_term.lower() == line:
                results.append(line)
    return results

find_words("vokes")
