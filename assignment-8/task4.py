lengths = int(input("Input the number of elements: "))
size = int(input("Input the size of each element: ")) + 1

# prints cells based on the size and lengths
for row in range(size+1):
    for column in range(lengths*size+1):
        if row % size == 0 and column % size == 0:
            print("+", end="")
        elif row % size != 0 and column % size == 0:
            print("|", end="")
        elif row % size == 0 and column % size != 0:
            print("-", end="")
        else:
            print(" ", end="")
    print()