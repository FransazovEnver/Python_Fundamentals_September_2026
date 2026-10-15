numbers_list = input().split()

absolute_values = []

for num in numbers_list:
    absolute_values.append(abs(float(num)))

print(absolute_values)
