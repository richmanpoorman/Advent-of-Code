file = open("input.txt", "r")

letters = [0] * 26
str = file.readline()

for i in range(14):
    letters[ord(str[i]) - 97] += 1

for i in range(14, len(str)):
    letters[ord(str[i]) - 97] += 1
    letters[ord(str[i - 14]) - 97] -= 1
    isGood = True
    for check in letters:
        if check >= 2:
            isGood = False
            break
    if isGood:
        print(i + 1)
        print(letters)
        break
        
file.close()