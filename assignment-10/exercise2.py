total_rows = 0
total_characters = 0
digit_count = 0
capital_letter_count = 0
small_letter_count = 0
spacing_count = 0
punctuation_count = 0
other_count = 0

with open("numbers.txt", 'r') as file:
    for line in file:
        total_rows += 1
        total_characters += len(line)

        for char in line:
            if char.isdigit():
                digit_count += 1
            elif char.isupper():
                capital_letter_count += 1
            elif char.islower():
                small_letter_count += 1
            elif char.isspace():
                spacing_count += 1
            elif char in ',.:;?!':
                punctuation_count += 1
            else:
                other_count += 1
print(f"Total number of rows: {total_rows}")
print(f"Total number of characters: {total_characters}")
print(f"Number of digits: {digit_count}")
print(f"Number of capital letters: {capital_letter_count}")
print(f"Number of small letters: {small_letter_count}")
print(f"Number of spacing characters: {spacing_count}")
print(f"Number of punctuation characters: {punctuation_count}")
print(f"Number of other characters: {other_count}")
