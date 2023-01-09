import re
file = open("input.txt", "r")

sum = 0
for x in file:
    data = re.split(",|-", x)
    # Entirely inside
    # if (int(data[0]) <= int(data[2]) and int(data[1]) >= int(data[3])) or (int(data[0]) >= int(data[2]) and int(data[1]) <= int(data[3])):
    
    # Overlap at all
    if not (int(data[1]) < int(data[2]) or int(data[0]) > int(data[3])):
        sum += 1
print(sum)
file.close()