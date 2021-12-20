import re

pattern = r"([0-9]*)-([0-9]*) ([a-z]): ([a-zA-Z]*)"
input_file = open("input.txt", "r")
lines = input_file.readlines()

valid_original = 0
valid_new = 0
for line in lines:
    match = re.match(pattern, line)
    if match:
        min = int(match.group(1))
        max = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        char_min = password[min-1]
        char_max = password[max-1]
        # print(password, char_min, char_max, character)
        if char_min == character or char_max == character:
            if char_min != char_max:
                # print(password)
                valid_new += 1

        count = password.count(character)
        if count >= min and count <= max:
            valid_original += 1


print(valid_new)
print(valid_original)
