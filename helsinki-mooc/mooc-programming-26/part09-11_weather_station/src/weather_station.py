# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, city):
        self.city = city
        self.__observations = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)

    def latest_observation(self):
        if len(self.__observations) == 0:
            return ""
        return self.__observations[-1]

    def number_of_observations(self):
        return len(self.__observations)

    def __str__(self):
        return f"{self.city}, {self.number_of_observations} observations"
