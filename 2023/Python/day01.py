def convert_str_to_int(line: str):
    str_to_int = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for k, v in str_to_int.items():
        if not k in line:
            continue
        while True:
            start = line.find(k)
            if start == -1: break
            line = line[:start + 1] + v + line[start + 1:]
    return line

def is_digit(c) -> bool:
    return c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def convert_two_digit(num: str) -> int:
    # convert n-digit number to two digit number
    return int(num[0] + num[-1])

with open("../inputs/day01.txt", "r") as f:
    lines = f.readlines()


lines_ = []
for line in lines:
    lines_ += [convert_str_to_int(line)]

print(sum([convert_two_digit("".join(filter(is_digit, line))) for line in lines_]))
