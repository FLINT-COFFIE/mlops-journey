# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# defining variables
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

# roots
x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
# output
print(f"The roots are {x1} and {x2}")
