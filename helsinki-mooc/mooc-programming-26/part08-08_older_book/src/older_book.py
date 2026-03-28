# DO NOT CHANGE CLASS Book!
# Write your solution after the class!


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


# -----------------------------
# Write your solution here
# -----------------------------


# defining the function
def older_book(book1: Book, book2: Book):
    difference = book1.year - book2.year
    if difference < 0:
        print(f"{book1.name} is older, it was published in {book1.year}")

    elif difference > 0:
        print(f"{book2.name} is older, it was published in {book2.year}")

    else:
        print(f"{book1} and {book2} were published in {book1.year}")
