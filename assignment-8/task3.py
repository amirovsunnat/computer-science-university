def power_fun(num):
    """Receives a number and returns power of this function."""
    return num ** num


def find_max_x(y):
    x = 0
    while power_fun(x) < y:
        x += 1
    return x - 1


number = int(input("Input x: "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    max_x = find_max_x(number)
    print(f"Maximum x = {max_x}")


