# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f"{self.name}, superpowers: {self.superpowers}"


class SuperGroup(SuperHero):
    def __init__(self, name: str, location: str):
        super().__init__(name)
        self._name = super().name
        self._location = location
        self._members = []
        
    # Getters
    
    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self.location

    # Add member method
    def add_member(self, hero: SuperHero):
        self.members.append(hero)
        
    # print_group method
    def print_group(self):
        