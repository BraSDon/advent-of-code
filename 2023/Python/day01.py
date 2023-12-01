def is_digit(c) -> bool:
    return c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def convert_two_digit(num: str):
    # convert n-digit number to two digit number
    if len(num) == 1:
        return int(num + num)
    elif len(num) > 2:
        return int(num[0] + num[-1])
    else:
        return int(num)

with open("./inputs/day01.txt", "r") as f:
    lines = f.readlines()

numbers = []
for line in lines:
    digits_only = "".join(filter(is_digit, line))
    numbers.append(convert_two_digit(digits_only))

print(sum(numbers))
