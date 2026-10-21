def sorted_numbers(numbers):
    int_nums = [int(index) for index in numbers]
    print(sorted(int_nums))

current_number = input().split()
sorted_numbers(current_number)