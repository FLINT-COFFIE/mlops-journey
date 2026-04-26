# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        # self.rate = rate
        self.count = 0
        self.add = 0

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.rating = rating
            self.count += 1
            self.add += rating

    def __str__(self):
        if self.count == 0:
            average = "no ratings"
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{average}"

        elif self.count > 0:
            average = self.add / self.count
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{self.count} ratings, average {average:.1f} points"


def minimum_grade(rating: float, series_list: list):
    found = []
    for serie in series_list:
        if serie.count > 0:
            if (serie.add / serie.count) >= rating:
                found.append(serie)
    return found


def includes_genre(genre: str, series_list: list):
    found = []
    for serie in series_list:
        if genre in serie.genres:
            found.append(serie)
    return found


if __name__ == "__main__":
    # testing
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
