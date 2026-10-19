def odd_even_sum(number: str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit_as_string in number:
        if int(digit_as_string) % 2 == 0:
            sum_of_even_digits += int(digit_as_string)
        else:
            sum_of_odd_digits += int(digit_as_string)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

number_as_string = input()
result = odd_even_sum(number_as_string)
print(result)