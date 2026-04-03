# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("The amount must not be below zero")
        else:
            self.__length = length

    # A getter method
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("The amount must not be below zero")
        else:
            self.__length = length


if __name__ == "__main__":
    # testing
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
