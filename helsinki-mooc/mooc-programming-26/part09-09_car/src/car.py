# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__gasoline = 0
        self.__odometer_reading = 0

    def fill_up(self):
        self.__gasoline = 60

    def drive(self, Km: int):
        distance_allowed = self.__gasoline
        if Km > distance_allowed:
            self.__odometer_reading = 60
            self.__gasoline = 0
        else:
            self.__odometer_reading += Km
            self.__gasoline = 60 - Km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__gasoline} litres"


if __name__ == "__main__":
    # testing
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
