
file = open("input.txt", "r")
sum = 0
fileLine = 0
num = 1
a = set()
b = set()
for x in file:
    
    if num % 3 == 0:
        for c in x:
            if c in b:
                if c.islower():
                    sum += ord(c) - 97 + 1
                else:
                    sum += ord(c) - 65 + 27
                break
    elif num % 3 == 1:
        a.clear()
        for c in x:
            a.add(c)
    else:
        b.clear()
        for c in x:
            if c in a:
                b.add(c)

    num += 1
print(sum)
file.close()
'''
sum = 0
num = 0
fileLine = 0
for x in file:
    fileLine += 1
    x.strip()
    half = int(len(x) / 2)
    print(fileLine, half)
    seen = set()
    for i in range(half):
        seen.add(x[i])
    for i in range(half):
        i += half
        if x[i] in seen:
            num += 1
            if x[i].islower():
                print("lower",x[i])
                sum += ord(x[i]) - 97 + 1
            else:
                print("Upper", x[i])
                sum += ord(x[i]) - 65 + 27
            break
file.close()
print(sum, num)'''