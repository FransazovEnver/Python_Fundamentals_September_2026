while True:
    reverse_string = input()

    if reverse_string == "end":
        break

    print(f"{reverse_string} = {reverse_string[::-1]}")