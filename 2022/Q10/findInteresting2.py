file = open("input.txt", "r")

counter = 0
strength = 1

outputs = [[]]

for x in file:
    x = x.strip()
    if x == "noop":
        if abs(strength - counter % 40) <= 1:
            outputs[-1].append("#")
        else:
            outputs[-1].append(".")
        
        counter += 1
        if counter % 40 == 0:
            outputs.append([])
    else:
        if abs(strength - counter % 40) <= 1:
            outputs[-1].append("#")
        else:
            outputs[-1].append(".")
        
        counter += 1
        if counter % 40 == 0:
            outputs.append([])
        
        if abs(strength - counter % 40) <= 1:
            outputs[-1].append("#")
        else: 
            outputs[-1].append(".")
        
        counter += 1
        if counter % 40 == 0:
            outputs.append([])

        val = int(x.split(" ")[1])
        strength += val 
    print(strength)

for x in outputs:
    print("".join(x))
        
'''
if counter % 60 == 1:
    total += (counter - 1) * strength
elif counter % 60 == 0:
    total += counter * strength
'''