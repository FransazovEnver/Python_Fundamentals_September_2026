numbers = input().split()

opposite_number = []

for num in numbers:
    current_number = - int(num)
    opposite_number.append(current_number)
print(opposite_number)