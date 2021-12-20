import re

input_file = open("customs.txt", "r")
data = input_file.read()
groups = data.split("\n\n")

count = 0
all_yes_count = 0
for group in groups:
    group_answers = []
    members = group.split("\n")
    for member in members:
        letters = set()
        group_answers.append(letters)
        for c in member:
            pattern = r"[a-z]"
            match = re.match(pattern, c)
            if match:
                letters.add(c)
    intersec = group_answers[0]
    for i in range(len(group_answers)):
        intersec = intersec.intersection(group_answers[i])

    all_yes_count += len(intersec)
    count += len(letters)

print(all_yes_count)
print(count)