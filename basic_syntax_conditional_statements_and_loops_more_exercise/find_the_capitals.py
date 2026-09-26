capital = input()
up_list = []

for index in range(len(capital)):
    if capital[index].isupper():
        up_list.append(index)
print(up_list)