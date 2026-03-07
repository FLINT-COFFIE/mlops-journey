# Write your solution here

# define read to open the file and extract info
def read(filename: str):
    with open(filename) as newfile:
        recipe_book = []
        for line in newfile:
            line = line.strip()
            recipe_book.append(line)
        return recipe_book


# def search_by_name(filename:str,word:str):
def search_by_name(filename: str, word: str):
    book = read(filename)
    word = word.lower()
    recipies = []
    for char in book:
        rec = []
        if char == " ":
            continue
        if word in char.lower():
            rec.append(char)
            recipies.append(rec)
    for food in recipies:
        return recipies[food]


print(search_by_name("recipes1.txt", "cake"))
