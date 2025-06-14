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

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("\033[91mValue must be greater than 0.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a numeric value.\033[0m")

def calc_area(a, b):
    return round(0.5 * a * b, 2)

def calc_perimeter(a, b, c):
    return round(a + b + c, 2)

def main():

    char_input = None
    a = None
    b = None
    c = None
    
    try:
        print("\n========== Pythagorean Theorem Calculator ==========\n") 
        while(1):
            char_input = input("Do you want to calculate side c (hypotenuse) or side a/b? (a/b/c or exit): ").strip().lower()
            if char_input == 'c':
                a = get_positive_float("\nEnter the length of side a: ")
                b = get_positive_float("Enter the length of side b: ")
                print(f"\n\033[92mThe length of side c (hypotenuse) is: {calc_side_c(a, b)}\033[0m")
                print(f"\033[92mThe area of the triangle is: {calc_area(a, b)}\033[0m")
                print(f"\033[92mThe perimeter of the triangle is: {calc_perimeter(a, b, calc_side_c(a, b))}\033[0m")
                break
            
            elif char_input == 'a':
                while True:
                    c = get_positive_float("\nEnter the length of side c (hypotenuse): ")
                    b = get_positive_float("Enter the length of side b: ")
                    if b >= c:
                        print("\033[91mSide b must be less than side c (hypotenuse).\033[0m")
                        continue
                    break

                print(f"\033[92m\nThe length of side a is: {calc_side_ab(b, c)}\033[0m")
                print(f"\033[92mThe area of the triangle is: {calc_area(b, c)}\033[0m")
                print(f"\033[92mThe perimeter of the triangle is: {calc_perimeter(b, c, calc_side_ab(b, c))}\033[0m")
                break

            elif char_input == 'b':
                while True:
                    c = get_positive_float("\nEnter the length of side c (hypotenuse): ")
                    a = get_positive_float("Enter the length of side a: ")
                    if a >= c:
                        print("\033[91mSide a must be less than side c (hypotenuse).\033[0m")
                        continue
                    break

                print(f"\033[92m\nThe length of side b is: {calc_side_ab(a, c)}\033[0m")
                print(f"\033[92mThe area of the triangle is: {calc_area(a, c)}\033[0m")
                print(f"\033[92mThe perimeter of the triangle is: {calc_perimeter(a, c, calc_side_ab(a, c))}\033[0m")
                break

            elif char_input == 'exit':
                print("\033[93m Exiting the program\033[0m")
                break
            else:
                print("\033[91mInvalid input. Please enter 'a', 'b', or 'c'.\033[0m\n")

    except KeyboardInterrupt:
        print("\n\033[93m Program interrupted. Exiting gracefully.\033[0m")

if __name__ == "__main__":
    main()