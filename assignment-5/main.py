# Exercise 1
# take numbers from user and store them into numbers
numbers = input("Enter numbers (4 8 9 2 4):\n>>>").split()
odd_numbers = []
even_numbers = []

for num in numbers:
    num = int(num)
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Odd numbers: {' '.join(map(str, odd_numbers))}")
print(f"Even numbers: {' '.join(map(str, even_numbers))}")

# exercise 2
n = int(input("Enter n: "))
if n > 100:
    print("Please enter number less than 100")
numbers_entered = []
for a in range(n):
    number = int(input(f"Input v[{a}]: "))
    numbers_entered.append(number)
while True:
    other_number = int(input("Input x: "))

    should_add_again = int(input(f"Value {other_number} appears {numbers_entered.count(other_number)} time(s) in the array."
                                 f"\nWould you like to continue (1=yes, 0=no) ? "))
    if should_add_again:
        numbers_entered.append(other_number)
    else:
        print("Program terminated.")
        break

# exercise 3
max_difference = 0
position = 0
v = input("Enter ten numbers (1 5 2 6)\n>>> ").split()
w = input("Enter another ten numbers (1 5 2 6)\n>>> ").split()
for i in range(len(v)):
    w_num = int(w[i])
    v_num = int(v[i])
    difference = w_num - v_num
    if difference > max_difference:
        max_difference = difference
        position = i
    else:
        continue

print(f"The max difference is {max_difference} on the index of {position}")

# exercise 4
bases = input("Enter the bases(1 2 5) on this format\n>>> ").split()
exponents = input("Enter the exponents on this format (4 8 2)\n>>> ").split()
powers = []
if len(bases) != len(exponents):
    print("Please make sure you have entered same length of numbers on both bases and exponents")
else:
    for i in range(len(bases)):
        bases_num = int(bases[i])
        exponents_num = int(exponents[i])
        powers.append(bases_num ** exponents_num)
print(powers)


# exercise 5
v = input("ENTER ANY NUMBERS: ").split()
n = len(v)
max_length = 0
current_length = 0
start_index = -1
current_start = -1
for i in range(n):
    if int(v[i]) > 0:
        if current_start == -1:
            current_start = i
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            start_index = current_start
        current_length = 0
        current_start = -1

if current_length > max_length:
    max_length = current_length
    start_index = current_start

if max_length > 0:
    print(f"The longest positive sequence ({max_length} elements) starts from index {start_index}.")
else:
    print("There are no consecutive positive values in the array.")
