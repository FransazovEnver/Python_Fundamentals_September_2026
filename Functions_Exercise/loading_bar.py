def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent_as_digit = some_number // 10
    not_loaded_percent_as_digit = 10 - loaded_percent_as_digit
    return f"{some_number}% [" \
           f"{'%' * loaded_percent_as_digit}" \
           f"{'.' * not_loaded_percent_as_digit}" \
           f"]\nStill loading..."

number = int(input())
print(loading_bar(number))