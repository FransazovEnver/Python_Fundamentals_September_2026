numbers = input().split(", ")
positive_numbers = [pos_number for pos_number in numbers if int(pos_number) >= 0]
negative_numbers = [neg_number for neg_number in numbers if int(neg_number) < 0]
even_numbers = [ev_number for ev_number in numbers if int(ev_number) % 2 == 0]
odd_numbers = [od_number for od_number in numbers if int(od_number) % 2 != 0]
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")