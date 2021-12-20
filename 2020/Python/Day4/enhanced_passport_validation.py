import re

input_file = open("passportData.txt", "r")
# input_file = open("textData.txt", "r")

data = input_file.read()
passports = data.split("\n\n")
valid_passports = 0

for passport in passports:
    temp = passport.replace("\n", " ")
    features = temp.split(" ")
    feature_names = []
    valid_features = True
    for feature in features:
        if not valid_features:
            break
        feature_info = feature.split(":")
        feature_names.append(feature_info[0])
        if feature_info[0] == "byr":
            valid_features = (int(feature_info[1]) >= 1920) and (int(feature_info[1]) <= 2002)
        elif feature_info[0] == "iyr":
            valid_features = (int(feature_info[1]) >= 2010) and (int(feature_info[1]) <= 2020)
        elif feature_info[0] == "eyr":
            valid_features = (int(feature_info[1]) >= 2020) and (int(feature_info[1]) <= 2030)
        elif feature_info[0] == "hgt":
            pattern = r"([0-9]*)(in|cm)"
            match = re.match(pattern, feature_info[1])
            if match:
                if match.group(2) == "in":
                    valid_features = int(match.group(1)) >= 59 and int(match.group(1)) <= 76
                else:
                    valid_features = int(match.group(1)) >= 150 and int(match.group(1)) <= 193
            else:
                valid_features = False
        elif feature_info[0] == "hcl":
            pattern = r"^(#)([0-9]|[a-f]){6}$"
            match = re.match(pattern, feature_info[1])
            if not match:
                valid_features = False
        elif feature_info[0] == "ecl":
            pattern = r"(amb|blu|brn|gry|grn|hzl|oth)"
            match = re.match(pattern, feature_info[1])
            if not match:
                valid_features = False
        elif feature_info[0] == "pid":
            pattern = r"^\d{9}$"
            match = re.match(pattern, feature_info[1])
            if not match:
                valid_features = False
    if valid_features:
        if len(feature_names) == 8:
            valid_passports += 1
        elif len(feature_names) == 7 and (not "cid" in feature_names):
            valid_passports += 1
        else:
            continue

print(valid_passports)

