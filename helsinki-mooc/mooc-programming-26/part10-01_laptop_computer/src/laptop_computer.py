# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed


## Inheritance of Computer for Laptop Computer
class LaptopComputer(Computer):
    def __init__(self, model, speed):
        super().__init__(model, speed)
