def calculate_factorial(number: int) -> int:
    for current_number in range(1, number):
        number *= current_number
    return number

first_number = int(input())
second_number = int(input())
first_result = calculate_factorial(first_number)
second_result = calculate_factorial(second_number)
final_result = first_result / second_result
print(f"{final_result:.2f}")