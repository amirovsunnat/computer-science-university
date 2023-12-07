# -----task 1-----
# array = [[4, 3, 1, 2], [1, 7, 2, 2], [3, 3, 5, 0]]
# sum_col = 0
# sum_row = [0, 0, 0, 0]
# for i in range(len(array)):
#     for j in range(len(array[0])):
#         sum_col += array[i][j]
#         print(array[i][j], end="\t")
#         sum_row[j] += array[i][j]
#     print(sum_col)
#     sum_col = 0
# print("\t".join(map(str, sum_row)))


# -----task 2-----
# array = [
#     [2.6, 4.4, 5.0],
#     [4.8, 3.4, 7.2],
#     [2.0, 2.6, 3.8],
# ]
#
#
# def add_extra_matrix(arr, length_of_elements):
#     empty_array = []
#     count = 1
#     for i in range(length_of_elements):
#         empty_array.append(0)
#         if i != length_of_elements - 1:
#             arr.insert(i + count, empty_array)
#         count = count + 1
#     return arr


# new_array = add_extra_matrix(array, 3)
# for j in range(len(new_array)):
#     for b in range(len(new_array[0])):
#         if j < len(new_array) - 1 and j == 1:
#             new_array[j][b] = round((new_array[j-1][b] + new_array[j+1][b]) / 2, 1)
#
# print(new_array)
#

# middle_array = [0, 0, 0]
# for k in range(len(array)):
#     for l in range(len(array[0])):
#         num = array[k][l]
#         print(num, end="\t")
#         if k < len(array) - 1:
#             num2 = array[k + 1][l]
#             num3 = round((num + num2) / 2, 1)
#             middle_array[l] = num3
#     print()
#     if k < len(array) - 1:
#         print(middle_array)


# -----task3-----

# # Get the dimensions of the matrix from the user
# def create_matrix(matrix_num):
#     rows = int(input(f"Enter the {matrix_num} matrix number of rows: "))
#     columns = int(input(f"Enter the {matrix_num} matrix number of columns: "))
#
#     # Initialize an empty matrix
#     matrix = []
#
#     # Take input for each element in the matrix
#     for i in range(rows):
#         row = []
#         for j in range(columns):
#             element = float(input(f"Enter the element at position ({i+1}, {j+1}): "))
#             row.append(element)
#         matrix.append(row)
#
#     return matrix
#
#
# matrix1 = create_matrix("first")
# matrix2 = create_matrix("second")
#
# col_len = len(matrix1[0])   # take length of column in the first matrix
# row_len = len(matrix2)  # take length of row in the second matrix
# # check if we can multiply two matrix
# # Check if matrices can be multiplied
# if col_len == row_len:
#     new_matrix = []
#     # Iterate through rows of the first matrix
#     for i in range(len(matrix1)):
#         row = []
#
#         # Iterate through columns of the second matrix
#         for j in range(len(matrix2[0])):
#             # Perform the dot product to calculate the element in the new matrix
#             element_sum = 0
#             for k in range(col_len):
#                 element_sum += matrix1[i][k] * matrix2[k][j]
#
#             row.append(element_sum)
#
#         new_matrix.append(row)
#
#     # Print the resulting matrix
#     print("Resulting Matrix:")
#     for row in new_matrix:
#         print(row)
#
# else:
#     print(
#         "Matrices cannot be multiplied. "
#         "The number of columns in the first matrix must be equal to the number of rows in the second matrix.")


# task 4
# row = int(input("Enter the length of the row: "))
# column = int(input("Enter the length of the column: "))
# matrix, sublist = [], []
#
# for x in range(row):
#     for y in range(column):
#         element = int(input("Enter the elements of the matrix: "))
#         sublist.append(element)
#     matrix.append(sublist)
#     sublist = []
#
#
# matrix = [
#     [1, -2, 0, 3],
#     [3, 1, 5, 4],
#     [7, 2, 3, 1],
#     [4, 6, -1, 5]
# ]
#
# top_left_matrix, top_right_matrix, bottom_left_matrix, bottom_right_matrix = [], [], [], []
#
# n = int(input("Enter a number: "))
# for row in matrix:
#     for column in row:
#         if n == column:
#             print(f"Number is situated at row {matrix.index(row) + 1}, and column {row.index(n)+1}")
#             for x in range(len(matrix)):
#                 for y in range(len(matrix)):
#                     if x < matrix.index(row) and y < row.index(n):
#                         top_left_matrix.append(matrix[x][y])
#                     elif x < matrix.index(row) and y > row.index(n):
#                         top_right_matrix.append(matrix[x][y])
#                     elif x > matrix.index(row) and y < row.index(n):
#                         bottom_left_matrix.append(matrix[x][y])
#                     elif x > matrix.index(row) and y > row.index(n):
#                         bottom_right_matrix.append(matrix[x][y])
#             if len(top_left_matrix) > 0:
#                 print(top_left_matrix)
#             if len(top_right_matrix) > 0:
#                 print(top_right_matrix)
#             if len(bottom_left_matrix) > 0:
#                 print(bottom_left_matrix)
#             if len(bottom_right_matrix) > 0:
#                 print(bottom_right_matrix)
#             top_left_matrix, top_right_matrix, bottom_left_matrix, bottom_right_matrix = [], [], [], []


# exercise 5
n = int(input("Enter n: "))
n_sum = 1
row = 0
column = 0
print(f"({row},{column})", end='   ')
flag = True
while flag:
    def print_it():
        print(f"({row},{column})", end='   ')
        global n_sum
        n_sum += 1
        if n_sum == n:
            print()
            n_sum = 0

    if column + 1 != n:
        column += 1
    else:
        row += 1
    print_it()

    while column - 1 >= 0 and row + 1 < n:
        row += 1
        column -= 1
        print_it()

    if row + 1 < n:
        row += 1
    else:
        column += 1
    print_it()

    while column + 1 < n and row - 1 >= 0:
        column += 1
        row -= 1
        print_it()

    if column + row == (n - 1) * 2:
        flag = False
