file_object = open("input.txt", "r")
lines = file_object.readlines()

for line in lines:
    i = int(line)
    for line in lines:
        j = int(line)
        for line in lines:
            k = int(line)
            if i+j+k == 2020:
                print(i + j + k , i * j * k)



