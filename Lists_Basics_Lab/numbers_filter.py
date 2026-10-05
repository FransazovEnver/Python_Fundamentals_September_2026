number = int(input())

some_numbers = []
for num in range(number):
    current_number = int(input())
    some_numbers.append(current_number)

command = input()
filtered_numbers = []

if command == "even":
    for num in some_numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)

elif command == "odd":
    for num in some_numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)

elif command == "negative":
    for num in some_numbers:
        if num < 0:
          filtered_numbers.append(num)

elif command == "positive":
    for num in some_numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)