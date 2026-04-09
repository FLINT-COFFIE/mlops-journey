# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


# secret potion
class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self._password = password

    # first method
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self._password:
            super().add_ingredient(ingredient, amount)

    # second method
    def print_recipe(self, password: str):
        if password == self._password:
            return super().print_recipe()
