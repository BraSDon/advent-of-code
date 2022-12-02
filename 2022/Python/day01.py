with open("inputs/day01.txt") as file:
    lines = file.readlines()
    calorie_lists = list()
    elf_calories = list()
    for line in lines:
        if line == "\n":
            calorie_lists.append(elf_calories)
            elf_calories = list()
        else:
            elf_calories.append(int(line))

sorted_calories = [sum(l) for l in calorie_lists]
sorted_calories.sort(reverse=True)
print(f"Max calories: {sorted_calories[0]}")
print(f"Top three summed: {sum(sorted_calories[:3])}")
