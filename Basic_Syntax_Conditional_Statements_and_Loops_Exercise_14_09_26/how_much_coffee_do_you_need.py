number_of_coffees = 0
command = input()

while command != "END":
    if command.islower():
        needed_coffee = 1
    else:
        needed_coffee = 2
    if command.lower() == "coding" or \
            command.lower() == "dog" or \
            command.lower() == "cat" or \
            command.lower() == "movie":
        number_of_coffees += needed_coffee
    command = input()
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
