file_name = input( "Enter the file name: ")

a = open(file_name, 'r')
values = []
for line in a:
    values.extend(map(int, line.split()))

num_values = len(values)
overall_sum = sum(values)
max_value = max(values)
min_value = min(values)

print(f"Number of values: {num_values}")
print(f"Overall sum: {overall_sum}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
