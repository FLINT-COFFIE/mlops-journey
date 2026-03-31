# Write your solution here:
class Series:
    def __init__(self, name: str, seasons: int, genres: list):
        self.name = name
        self.seasons = seasons
        self.genres = genres

    def __str__(self):
        return f"{self.name} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\nno ratings"


# testing
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)
