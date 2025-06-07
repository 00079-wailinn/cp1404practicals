import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


"""
on line 1 after running, the output is 19. And the biggest number could be 19, while the smallest is 5.

on line 2 after running, the output is 5. And the biggest number could be 10, while the smallest is 3.
line 2 could not produce a 4 because the increment value is 2.

on line 3 after running, the output is 4.360436137560125. And the biggest number could be 5.5, while the smallest is 2.5.

"""