# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def ratings(item):
        return item["rating"]
    return sorted(items, key=ratings)
