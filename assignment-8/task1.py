num1, num2 = input("Enter numbers in this format: (15/45): ").split("/")
num1 = int(num1)
num2 = int(num2)

n1 = num1
n2 = num2

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        n1 = num1 // i
        n2 = num2 // i

print(f"Simplified fraction: {n1}/{n2}")
