# Write your solution here
# import
from math import sqrt


# defining function
def hypotenuse(leg1: float, leg2: float):
    final_leg = sqrt((leg1**2) + (leg2**2))
    return final_leg


if __name__ == "__main__":
    print(hypotenuse(3, 4))  # 5.0
    print(hypotenuse(5, 12))  # 13.0
    print(hypotenuse(1, 1))  # 1.4142135623730951
