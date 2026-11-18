string_emoticon = input()
emoticon = ""
for index in range(len(string_emoticon)):
    if string_emoticon[index] == ":":
        print(f":{string_emoticon[index + 1]}")