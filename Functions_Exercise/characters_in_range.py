def ascii_characters(first: str, second: str) -> list:
    all_the_characters = []
    for character_as_digit in range(ord(first) + 1, ord(second)):
        all_the_characters.append(chr(character_as_digit))
    return all_the_characters

first_string = input()
second_string = input()
result_as_list = ascii_characters(first_string, second_string)
print(" ".join(result_as_list))