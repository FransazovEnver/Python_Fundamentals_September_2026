sheep = input().split(", ")

wolf = sheep.index("wolf")
if wolf == len(sheep)-1:
    print("Please go away and stop eating my sheep")
else:
    number_sheep = len(sheep) - 1 - wolf
    print(f"Oi! Sheep number {number_sheep}! You are about to be eaten by a wolf!")