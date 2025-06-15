"""

numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

"""

numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
# 3

print(numbers[-1])
# 2

print(numbers[3])
# 1

print(numbers[:-1])
# [3, 1, 4, 1, 5, 9]

print(numbers[3:4])
# [1]

print(5 in numbers)
# True

print(7 in numbers)
# False

print("3" in numbers)
# False

print(numbers + [6, 5, 3])
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = 'ten'
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(f"is 9 in the number lists: {9 in numbers}")