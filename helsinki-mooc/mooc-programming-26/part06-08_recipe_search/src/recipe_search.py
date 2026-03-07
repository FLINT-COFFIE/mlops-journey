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


# define search by time
def search_by_time(filename: str, prep_time: int):
    recipes = read(filename)
    # store names
    output = []
    names = []
    times = []
    for recipe in recipes:
        time = int(recipe[1])
        name = recipe[0]
        if time <= prep_time:
            names.append(name)
            times.append(time)
    for i in range(len(names)):
        output.append(f"{names[i]}, preparation time {times[i]} min")
    return output


# search by ingredient
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read(filename)
    ingredients = []
    output = []
    names = []
    for item in recipes:
        # name = item[0]
        time = item[1]
        name = item[0]
        ingredients.append(item[2:])
        for prep in ingredients:
            if ingredient in prep:
                if name in names:
                    continue
                names.append(name)
                output.append(f"{name}, preparation time {time} min")

    return output


search_by_ingredient("recipes1.txt", "milk")

# search_by_time("recipes1.txt", 20)

if __name__ == "__main__":
    search_by_name("recipes1.txt", "cake")
    search_by_time("recipes1.txt", 20)
    search_by_ingredient("recipes1.txt", "eggs")
