def is_digit(c) -> bool:
    return c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def convert_two_digit(num: str) -> int:
    # convert n-digit number to two digit number
    return int(num[0] + num[-1])

with open("./inputs/day01.txt", "r") as f:
    lines = f.readlines()

numbers = []
for line in lines:
    digits_only = "".join(filter(is_digit, line))
    numbers.append(convert_two_digit(digits_only))

print(sum(numbers))
