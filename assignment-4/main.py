# task 1
# a)
"""for i in range(10):
    for a in range(10):
        print(f"{(i, a)} ", end="")
    print()"""

# b)
# for a in range(10):
#     for j in range(10):
#         if a == 0:
#             print(f" {j}\t", end=" ")
#         else:
#             print(f"{a}{j}\t", end=" ")
#     print()
# task 2
side = int(input("How many sides of figure do you want to draw?\n>>> "))
# a)
"""for i in range(side):
    print(f"*" * (side-i))"""

# b)
"""for i in range(side):
    print((i * " ") + "*" * side)"""

# c)
"""for i in range(side):
    if i == 0 or i == side-1:
        print("*" * side)
    else:
        print("*" + (side - 2) * " " + "*")"""

# d) 
"""for i in range(side):
    print((i * "-") + "*" + (side - (i + 1)) * "+")"""
    
# e)
# we need two variables in order to track column and row
row_num = 0
column_num = side - 1
for i in range(side):
    for j in range(side):
        if i == row_num and j == column_num:
            print("*", end="")
            row_num += 1
            column_num -= 1
        elif i == j:
            print("*", end="")
        else:
            print(end=" ")
    print()
# task 3
"""while True:
    n = int(input("Enter n: "))
    if n > 0:
        print(n * "*")
    else:
        print("Program terminated.")
        break"""

# task 4
# a)
# n = int(input("Enter n: "))
"""count = 1
for i in range(n):
    for j in range(i + 1):
        print(f"{count} ", end="")
        count += 1
    print()"""

# b)
# count = 1
# for i in range(n):
#     for j in range(i + 1):
#         if count <= n:
#             print(count, end=" ")
#             count += 1
#     print()
#     if count == n + 1:
#         break
