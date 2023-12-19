file_name = input("Enter a file name: ")

with open(file_name, 'r') as file:
    lines = file.readlines()
    matrix = [[int(i) for i in line.strip()] for line in lines]

rows = len(matrix)
cols = len(matrix[0])
n = 1

print(cols * "------" + "-")
for i in range(rows):
    for k in range(4):
        for j in range(cols):
            if matrix[i][j] == 0:
                print(f"|     ", end="")
            else:
                print("|*****", end="")
        print("|")

    if i < rows - 1:
        print("------" * cols + "-")

print(cols * "------" + "-")


print("\n\n")
print(cols * "------" + "-")

for i in range(rows):
    for k in range(4):
        for j in range(cols):
            if matrix[i][j] == 0:
                try:
                    one = (matrix[i + 1][j] == 0 and (i == 0 or matrix[i - 1][j] == 1))
                except IndexError:
                    one = False
                try:
                    two = (matrix[i][j + 1] == 0 and (j == 0 or matrix[i][j - 1] == 1))
                except IndexError:
                    two = False

                if k == 0 and (one or two):
                    if n > 99:
                        print(f"| {n} ", end="")
                    elif n > 9:
                        print(f"|  {n} ", end="")
                    else:
                        print(f"|   {n} ", end="")
                    n += 1
                else:
                    print(f"|     ", end="")
            else:
                print("|*****", end="")
        print("|")

    if i < rows - 1:
        print("------" * cols + "-")

print(cols * "------" + "-")

