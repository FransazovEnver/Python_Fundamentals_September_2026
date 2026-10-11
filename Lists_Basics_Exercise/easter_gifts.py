names_of_the_gifts = input().split()

command = input()
while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for gift_index in range(len(names_of_the_gifts)):
            if command[1] in names_of_the_gifts[gift_index]:
                names_of_the_gifts[gift_index] = "None"
    elif "Required" in command:
        for gift in range(len(names_of_the_gifts)):
            if gift == int(command[2]):
                names_of_the_gifts[gift] = command[1]
    elif "JustInCase" in command:
        names_of_the_gifts[-1] = command[1]
    command = input()
while "None" in names_of_the_gifts:
    names_of_the_gifts.remove("None")
for index in names_of_the_gifts:
    print(index, end=" ")