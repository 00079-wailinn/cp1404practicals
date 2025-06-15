"""
   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2
"""

# 1. Number list, min, max, average, first, last
numbers = []
total = 0
for i in range(5):
    number = int(input("Number: "))
    total += number
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is {total / len(numbers)}")

# print(numbers)


# 2. Username accessed
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

user_name = input("Enter username: ")
if user_name in usernames:
    print("Access granted.")
else:
    print("Access denied.")