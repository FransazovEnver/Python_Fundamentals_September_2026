characters = input()
letters = {}
for character in characters:
    if character == " ":
        continue
    if character not in letters.keys():
        letters[character] = 1
    else:
        letters[character] += 1
for char, occurences in letters.items():
    print(f"{char} -> {occurences}")