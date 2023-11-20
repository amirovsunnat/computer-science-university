# exercise 1
"""v = [18, 11, -4, 5, 0, 0, -2, 3, 25, 0]
pos_nums = []
neg_nums = []
for i in v:
    if i == 0:
        continue
    elif i % 2 == 0:
        pos_nums.append(i)
    else:
        neg_nums.append(i)

print(f"The positive numbers: {pos_nums}")
print(f"The negative numbers: {neg_nums}")"""

# exercise 2
"""nums = []
for i in range(200):
    number = int(input(f"Enter the {i+1} number: "))
    if number > 0:
        if number in nums:
            continue
        else:
            nums.append(number)
    else:
        print("You are not allowed to enter negative number.")
        break
print(" ".join(map(str, nums)))"""

# exercise 3
"""v = [2, -3, 1, 2, 3, 1, 4, -6, 7, -5, -1]
positions = []
sub_arrays = []
for i in range(len(v)):
    for j in range(i, len(v)):
        subarray = v[i:j + 1]
        if sum(subarray) == 0:
            sub_arrays.append(subarray)
            positions.append(i)
if sub_arrays:
    for s, p in zip(sub_arrays, positions):
        print(f"Sub-array starting from index {p}, length {len(s)}.")
else:
    print("No sub-arrays found with a sum of 0.")"""

# exercise 4
"""v = [10, 20, 30, 40, 50, 60, 70, 80]
triplets = []
for i in range(1, len(v)):
    if i == len(v)-1:
        print(f"Triplet {i}: {v[i]}+{v[0]}+{v[1]} = {v[i]+v[0] + v[1]}")
    elif i == len(v)-2:
        print(f"Triplet {i}: {v[i]}+{v[-1]}+{v[0]} = {v[i]+v[-1] + v[0]}")
    else:
        print(f"Triplet {i}: {v[i]}+{v[i+1]}+{v[i+2]} = {v[i]+v[i+1]+v[i+2]}")
"""

# extra
v = [10, 20, 30, 40, 50, 60, 70, 80]
num = 0


def delete_item(index, items):
    if index <= len(items) - 1:
        items.pop(index)
    else:
        return "Please enter valid position"
    return items


n = int(input("In which position number you want to delete? "))
for i in range(len(v)):
    if len(v) == 1:
        print(num)
    v = delete_item(n, v)

# exercise 5
# numbers = [1, 2, 3, 4, 5, 10, 20, 24, 55, 62, 73, 74, 89, 93, 95, 94]
# take number until it is less than 0 or more than 100, and save it to numbers list
# while True:
#     number = int(input("Enter number between 0 and 100\n>>> "))
#     if not number < 0 and number < 100:
#         numbers.append(number)
#     else:
#         break

# nums9 = 0
# nums10 = 10
# nums20 = 20
# nums30 = 30
# nums40 = 40
# nums50 = 50
# nums60 = 60
# nums70 = 70
# nums80 = 80
# nums90 = 90
# numbers2 = []
# for num in numbers:
#     if 0 <= num < 10:
#         numbers2.append(f"0{nums9}")
#         nums9 += 1
#     elif 10 <= num < 20:
#         numbers2.append(f"{nums10}")
#         nums10 += 1
#     elif 20 <= num < 30:
#         numbers2.append(f"{nums20}")
#         nums20 += 1
#     elif 30 <= num < 40:
#         numbers2.append(f"{nums30}")
#         nums30 += 1
#     elif 40 <= num < 50:
#         numbers2.append(f"{nums40}")
#         nums40 += 1
#     elif 50 <= num < 60:
#         numbers2.append(f"{nums50}")
#         nums50 += 1
#     elif 60 <= num < 70:
#         numbers2.append(f"{nums60}")
#         nums60 += 1
#     elif 70 <= num < 80:
#         numbers2.append(f"{nums70}")
#         nums70 += 1
#     elif 80 <= num < 90:
#         numbers2.append(f"{nums80}")
#         nums80 += 1
#     elif 90 <= num < 100:
#         numbers2.append(f"{nums90}")
#         nums90 += 1
#
# for i in range(10):
#     for j in range(10):
#         if f"{j}{i}" in numbers2:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
