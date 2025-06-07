"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_valid_input = False

while not is_valid_input:
    try:
        result = int(input("Enter a valid integer: "))
        is_valid_input = True  # Input was valid, so exit the loop
    except ValueError:
        print("That is not a valid integer. Please try again.")

print(f"You entered the integer: {result}")