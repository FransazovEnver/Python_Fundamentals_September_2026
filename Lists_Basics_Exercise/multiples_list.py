factor = int(input())
count = int(input())
numbers = []

for multi in range(1, count + 1):
    numbers.append(factor * multi)
print(numbers)