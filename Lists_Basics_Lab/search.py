number = int(input())
special_word = input()

list_word = []

for _ in range(number):
    some_string = input()
    list_word.append(some_string)
print(list_word)
for current_string in range(len(list_word)-1, -1, -1):
    element = list_word[current_string]
    if special_word not in element:
        list_word.remove(element)
print(list_word)
