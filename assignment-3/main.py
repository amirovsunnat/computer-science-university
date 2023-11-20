# exercise 1
"""a = int(input("How many numbers you want to add?\n>>> "))
total = 0
for i in range(a):
    number = int(input(f"Enter the {i+1} number: "))
    total += number
print(f"Average is {total/a}")"""

# exercise 2
"""num = int(input("Enter a number here\n>>> "))
summ = 0
for i in range(1, num+1):
    sum += (1 / i)
print(round(summ, 2))
"""

# exercise 3
"""total_positives = 0
total_negatives = 0
while True:
    n = int(input("Enter any integer number here\n>>> "))
    if n == 0:
        break
    elif n > 0:
        total_positives += n
    else:
        total_negatives += n
print(f"Total positive numbers: {total_positives}")
print(f"Total negative numbers: {total_negatives}")"""

# exercise 4
"""for i in range(65, 91):
    print(f"'{chr(i)}'\t\t{i}\t\t'{chr(i+32)}'\t\t{i+32}")"""

# exercise 5
x = int(input("Enter the first number\n>>> "))
y = int(input("Enter the second number\n>>> "))
small_number = min(x, y)
answer = 0
for i in range(1, small_number+1):
    if small_number % i == 0:
        if x % i == 0:
            answer = i
print(answer)

# exercise 6
"""n = int(input("How many numbers you want to add?\n>>> "))
old_number = int(input("Enter the first number\n>>> "))
is_dec = True
is_asc = True
for i in range(n-1):
    new_num = int(input(f"Enter the {i+2} number: "))
    if old_number > new_num:
        is_asc = False
    else:
        is_dec = False
if not is_dec and not is_asc:
    print("Neither descending nor ascending")
elif is_dec:
    print("Numbers in descending order.")
else:
    print("Numbers in ascending order.")"""

# exercise 7
number_of_elements = int(input("How many numbers you want to add?\n>>> "))
if number_of_elements < 2:
    print("Please enter at least 2 numbers.")
largest_number = int(input("Enter the first number: "))
second_largest_number = int(input("Enter the second number: "))
min_number = 0
for i in range(number_of_elements-2):
    num = int(input(f"Enter the {i + 2} number: "))
    if num > largest_number:
        largest_number = num
    else:
        min_number = num
print(largest_number)
print(min_number)
