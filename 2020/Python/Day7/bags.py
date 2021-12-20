import re

input_file = open("bags.txt", "r")
lines = input_file.readlines()

# bag_pattern = r"[a-z]* [a-z]* bags?"
# pattern = r"[a-z]* [a-z]* bags? contain [0-9] [a-z]* [a-z]* bags?.?"
# pattern = r"([a-z]* [a-z]*) bags contain (([0-9] ([a-z]* [a-z]*) (bag|bags),?\s)*)([0-9] ([a-z]* [a-z]*) (bag|bags))."
