file = open("data.txt", "r")

maxVal1 = 0
maxVal2 = 0
maxVal3 = 0
val = 0
for x in file:
    x = x.strip()
    if x == "":
        if maxVal1 < val:
            maxVal3 = maxVal2
            maxVal2 = maxVal1
            maxVal1 = val
        elif maxVal2 < val:
            maxVal3 = maxVal2
            maxVal2 = val 
        elif maxVal3 < val:
            maxVal3 = val
        val = 0
    else:
        val += int(x)
print(maxVal1 + maxVal2 + maxVal3)
file.close()