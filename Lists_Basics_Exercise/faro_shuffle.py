deck_of_cards = input().split()
number_of_cards = int(input())
for current_shuffle in range(number_of_cards):
    middle_of_the_desk = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_desk]
    right_part = deck_of_cards[middle_of_the_desk:]
    deck_after_shuffling = []
    for index in range(len(left_part)):
        deck_after_shuffling.append(left_part[index])
        deck_after_shuffling.append(right_part[index])
    deck_of_cards = deck_after_shuffling
print(deck_of_cards)