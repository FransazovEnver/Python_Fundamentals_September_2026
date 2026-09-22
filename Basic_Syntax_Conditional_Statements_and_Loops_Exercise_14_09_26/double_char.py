current_string = input()

while current_string != "End":
    if current_string != "SoftUni":
        final_string = ""
        for symbol in current_string:
            final_string += symbol * 2
        print(final_string)
    current_string = input()