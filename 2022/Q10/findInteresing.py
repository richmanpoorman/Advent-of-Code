file = open("input.txt", "r")

counter = 0
strength = 1
total = 0
for x in file:
    
    x = x.strip()
    if x == "noop":
        counter += 1
        if (counter - 20) % 40 == 0:
            total += counter * strength
        continue 
    counter += 2
    if (counter - 20) % 40 == 0:
        total += counter * strength
    elif (counter - 20) % 40 == 1:
        total += (counter - 1) * strength
    val = int(x.split(" ")[1]) - 1
    strength += val 
    

print (counter)
        
'''
if counter % 60 == 1:
    total += (counter - 1) * strength
elif counter % 60 == 0:
    total += counter * strength
'''
print(total)