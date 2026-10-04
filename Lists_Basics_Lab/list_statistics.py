numbers = int(input())

positive = []
negative = []

for _ in range(numbers):
    list_numbers = int(input())
    if list_numbers >= 0:
        positive.append(list_numbers)
    else:
        negative.append(list_numbers)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")