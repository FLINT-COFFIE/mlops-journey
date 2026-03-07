# Write your solution here

# define read to open the file and extract info
def read(filename: str):
    # open the file
    with open(filename) as newfile:
        # helper lists
        recipe_book = []
        current_recipe = []
        # looping through lines
        for line in newfile:
            line = line.strip()
            # grouping the data
            if line == "":
                if len(current_recipe) > 0:
                    recipe_book.append(current_recipe)
                # reset
                current_recipe = []
            else:
                current_recipe.append(line)
        if len(current_recipe) > 0:
            recipe_book.append(current_recipe)

        return recipe_book


filename = "recipes2.txt"
print(read(filename))


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
    food_name = []
    for food in recipies:
        food_name.append(food[0])
    # return i (for i in food_name:)


# print(search_by_name("recipes1.txt", "cake"))
