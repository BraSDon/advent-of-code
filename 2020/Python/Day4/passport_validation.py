input_file = open("passportData.txt", "r")

data = input_file.read()
passports = data.split("\n\n")
valid_passports = 0

for passport in passports:
    temp = passport.replace("\n", " ")
    features = temp.split(" ")
    feature_names = []
    for feature in features:
        feature_info = feature.split(":")
        feature_names.append(feature_info[0])
    if len(feature_names) == 8:
        valid_passports += 1
    elif len(feature_names) == 7 and (not "cid" in feature_names):
        valid_passports += 1
    else:
        continue

print(valid_passports)
