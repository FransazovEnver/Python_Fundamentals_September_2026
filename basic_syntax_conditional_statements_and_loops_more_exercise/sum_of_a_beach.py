some_text = input()
text = some_text.lower()
words = ["sand", "water", "fish", "sun"]
count = 0
for word in words:
    count += text.count(word)
print(count)
