money_as_string = input().split(", ")
numbers_of_beggars = int(input())
money_as_integer = []

for money in money_as_string:
    money_as_integer.append(int(money))
beggar_sum = []
start_index = 0

for current_beggar in range(numbers_of_beggars):
    current_begar_sum = 0
    for index in range(start_index, len(money_as_integer), numbers_of_beggars):
        current_begar_sum += money_as_integer[index]
    beggar_sum.append(current_begar_sum)
    start_index += 1
print(beggar_sum)