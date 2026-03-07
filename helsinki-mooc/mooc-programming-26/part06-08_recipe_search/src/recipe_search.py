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


# def search_by_name(filename:str,word:str):
def search_by_name(filename: str, word: str):
    book = read(filename)
    word = word.lower()

    # store food names
    names = []

    # loop through recipe
    for recipe in book:
        name = recipe[0]
        if word in name.lower():
            names.append(name)
    return names


search_by_name("recipes1.txt", "cake")
