LENGTH = int(input("Enter length: "))

with open("exercise_3.txt") as file:
    for line in file:
        words = line.split()
        spaces_to_add = LENGTH - len(line.strip())
        if len(words) > 1:
            spaces_between_words = spaces_to_add // (len(words) - 1)
            extra_spaces = spaces_to_add % (len(words) - 1)

            justified_line = words[0]
            for i in range(1, len(words)):
                justified_line += ' ' * (spaces_between_words + (1 if i <= extra_spaces else 0)) + words[i]
            with open("outputfile.txt", "a") as output:
                output.write(justified_line + '\n')