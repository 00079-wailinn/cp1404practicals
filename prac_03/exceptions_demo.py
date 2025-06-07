"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user inputs a non-integer value when prompted for the numerator or denominator
(e.g., entering a string or float instead of an integer).

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator, as division by zero is not allowed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid the possibility of a ZeroDivisionError, you can add a check before performing the division:

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")