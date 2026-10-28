first_sequence = input().split(", ")
second_sequence = input().split(", ")
mach_text = [first_string for first_string in first_sequence
             if any(first_string in second_string for second_string in second_sequence)]

print(mach_text)
