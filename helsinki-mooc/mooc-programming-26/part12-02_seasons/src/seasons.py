# Write your solution here:
def sort_by_seasons(items: list):
    def seasons(items):
        return [items[i]["seasons"] for i in items]
    return sorted(items, key=seasons(items))

