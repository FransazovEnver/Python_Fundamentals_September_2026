first_numbers = int(input())

for num in range(first_numbers):
    numbers = int(input())
    if not numbers % 2 == 0:
        print(f"{numbers} is odd!")
        break
else:
    print("All numbers are even.")