numbers = input().split()
number_to_remove = int(input())
left_numbers = [int(element) for element in numbers]
for num in range(1, number_to_remove + 1):
    min_number = min(left_numbers)
    left_numbers.remove(min_number)
print(", ".join(map(str, left_numbers)))
