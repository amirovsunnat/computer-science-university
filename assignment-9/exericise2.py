word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

distinct_letters = []
for letter in word1:
    if letter not in word2:
        distinct_letters.append(letter)
print(distinct_letters)
