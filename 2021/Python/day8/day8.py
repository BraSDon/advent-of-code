from collections import defaultdict
from functools import reduce

def split_at_pipe(line):
    input = line.split("|")[0].strip()
    output = line.split("|")[1].strip()
    return (input, output)

def mapToInt(line):
    mapping = {2: 1, 3: 7, 4: 4, 7: 8}
    result = list()
    output = line.split("|")[1].strip()
    output_words = output.split(" ")
    for word in output_words:
        try:
            result.append(mapping[len(word)])
        except KeyError:
            # Ignore for now
            pass
    return result

def findMapping(input_list):
    char_occurences = defaultdict(int)
    # Maps from new wires to original wires
    wire_mapping = dict()
    for word in input_list:
        for char in word:
            char_occurences[char] += 1
        if len(word) == 4:
            four_in_chars = list(word)
    for key, value in char_occurences.items():
        if value == 8:
            if key in four_in_chars:
                wire_mapping[key] = 'c'
            else:
                wire_mapping[key] = 'a'
        elif value == 7:
            if key in four_in_chars:
                wire_mapping[key] = 'd'
            else:
                wire_mapping[key] = 'g'
        elif value == 6:
            wire_mapping[key] = 'b'
        elif value == 4:
            wire_mapping[key] = 'e'
        elif value == 9:
            wire_mapping[key] = 'f'
    return wire_mapping

def get_decoded_output(wire_mapping, output):
    output_number = list()
    for word in output:
        decoded_word = set()
        for c in word:
            decoded_word.add(wire_mapping[c])
        output_number.append(segment_mapping[frozenset(decoded_word)])
    s = reduce(lambda x,y: x+str(y), output_number, '')
    return int(s) 

def sumDictValues(my_dict):
    return sum([value for value in my_dict.values()])

segment_mapping = {
        frozenset("abcefg"): 0,
        frozenset("cf"): 1,
        frozenset("acdeg"): 2, 
        frozenset("acdfg"): 3,
        frozenset("bcdf"): 4,
        frozenset("abdfg"): 5,
        frozenset("abdefg"): 6,
        frozenset("acf"): 7,
        frozenset("abcdefg"): 8, 
        frozenset("abcdfg"): 9
}

with open("2021\\Python\\day8\\input.txt") as f:
    lines = f.readlines()
    count = {1: 0, 4: 0, 7: 0, 8: 0}
    for line in lines:
        results = mapToInt(line)
        for result in results:
            count[result] += 1
    print(sumDictValues(count))

    output_numbers = list()
    for line in lines:
        input, output = split_at_pipe(line)
        wire_mapping = findMapping(input.split(" "))
        output_numbers.append(get_decoded_output(wire_mapping, output.split(" ")))
    
    print(sum(output_numbers))
