
file = open("input.txt", "r")

# X = Rock, Y = Paper, Z = Scissors
# A = Rock, B = Paper, C = Scissors
# X = Lose, Y = Draw , Z = Win
total = 0
for x in file:
    if x[2] == 'X':
        if x[0] == 'A':
            total += 3
        elif x[0] == 'B':
            total += 1
        elif x[0] == 'C':
            total += 2
    elif x[2] == 'Y':
        total += 3
        if x[0] == 'A':
            total += 1
        elif x[0] == 'B':
            total += 2
        elif x[0] == 'C':
            total += 3
    elif x[2] == 'Z':
        total += 6
        if x[0] == 'A':
            total += 2
        elif x[0] == 'B':
            total += 3
        elif x[0] == 'C':
            total += 1
'''
for x in file:
    score = 0
    if x[2] == 'X': # Rock
        score += 1
        if x[0] == 'A':
            score += 3
        elif x[0] == 'C':
            score += 6
    elif x[2] == 'Y': # Paper
        score += 2
        if x[0] == 'B':
            score += 3
        elif x[0] == 'A':
            score += 6
    elif x[2] == 'Z': # Scissor
        score += 3
        if x[0] == 'C':
            score += 3
        elif x[0] == 'B':
            score += 6

    if score == 0:
        print("ERROR")
    total += score
'''
print(total)
file.close()