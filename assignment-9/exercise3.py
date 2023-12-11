character = input("Input a character: ")
words = []
while True:
    word = input("Enter a word: ")
    if word == "stop":
        break
    words.append(word)

word_len_of_chars = {char: char.count(character) for char in words}
w = "".join([key for key, value in word_len_of_chars.items()
             if value == max(word_len_of_chars.values())])
print(f"The word with the most '{character}' is {w}")
