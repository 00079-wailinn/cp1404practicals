"""
languages
Estimate: 15 minutes
Actual: 18 minutes
"""

from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

gibson = Guitar(name, year, cost)
another_guitar = Guitar('Another Guitar', 2013, 1700)

print(f"{gibson.name} get_age() - Expect {102}. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expect {11}. Got {another_guitar.get_age()}")
print()

print(f"{gibson.name} is_vintage() - Expected {True}. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")
print()

print(gibson)
print(another_guitar)