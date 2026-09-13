word = input()

reversed_word = ""

for one_word in range(len(word) -1, -1, -1):
    reversed_word += word[one_word]
print(reversed_word)