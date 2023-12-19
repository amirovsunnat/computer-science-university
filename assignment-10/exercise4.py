# Read students file
import math

students_data = {}
with open("students.txt", 'r') as students_file:
    for line in students_file:
        name, matricula = line.strip().split()
        students_data[matricula] = name

# Read marks file
marks_data = {}
with open("marks.txt", 'r') as marks_file:
    for line in marks_file:
        matricula, mark1, mark2 = map(int, line.strip().split())
        matricula = str(matricula)
        marks_data[matricula] = (mark1, mark2)

# Calculate and print final marks
for matricula, name in students_data.items():
    if matricula in marks_data:
        mark1, mark2 = marks_data[matricula]
        average = math.ceil((mark1 + mark2) / 2)
        if mark1 < 15 or mark2 < 15 or average < 18:
            print(f"{name} FAIL")
        else:
            print(f"{name} {average}")
