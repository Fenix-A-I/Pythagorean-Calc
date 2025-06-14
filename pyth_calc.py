'''
Pythagorean Theorem Calculator
Goal: Refresh on using Python
Author: Alexandr Iapara
'''

# Importing math module
import math

# Function calculates the length of the hypotenuse (c)
def calc_side_c(a, b):
    # c^2 = a^2 + b^2
    return round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

# Function calculates the length of side a or b given the hypotenuse (c) and the other side
def calc_side_ab(ab, c):
    # a^2 = c^2 - b^2
    # b^2 = c^2 - a^2
    return round(math.sqrt(pow(c, 2) - pow(ab, 2)), 2)