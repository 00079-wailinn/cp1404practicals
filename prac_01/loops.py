for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(10, 101, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

number_star = int(input("Number of stars: "))
for i in range(number_star):
    print((i + 1) * '*')