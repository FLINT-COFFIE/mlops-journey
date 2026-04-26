# Write your solution here
# starting fractionate

# importing fractions
from fractions import Fraction


# defining the function
def fractionate(amount: int) -> Fraction:
    pieces = []
    frac = Fraction(1, amount)

    for i in range(amount):
        pieces.append(frac)
    return pieces


if __name__ == "__main__":
    print(fractionate(5))
