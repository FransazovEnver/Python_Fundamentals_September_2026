number_of_symbol = int(input())
for first_symbol in range(97, 97 + number_of_symbol):
    for second_symbol in range(97, 97 + number_of_symbol):
        for third_symbol in range(97, 97 + number_of_symbol):
            print(f"{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}")
