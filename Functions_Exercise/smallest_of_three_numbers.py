def find_smallest_number(list_with_numbers: list) -> int:
    return min(list_with_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())
result = find_smallest_number([first_number, second_number, third_number])
print(result)