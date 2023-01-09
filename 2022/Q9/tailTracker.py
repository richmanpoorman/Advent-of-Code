file = open("input.txt", "r")

headX = 0
headY = 0
tailX = 0
tailY = 0
visited = set()

visited.add((0, 0))
def updateTail():
    global tailX, tailY, headX, headY, visited
    if abs(headX - tailX) <= 9 and abs(headY - tailY) <= 9:
        return 
    if headX == tailX:
        if tailY < headY - 1:
            tailY += 1
        elif tailY > headY + 1:
            tailY -= 1
    elif headY == tailY:
        if tailX < headX - 1:
            tailX += 1
        elif tailX > headX + 1:
            tailX -= 1
    else:
        if headX < tailX and headY < tailY:
            tailX -= 1
            tailY -= 1
        elif headX < tailX and headY > tailY:
            tailX -= 1
            tailY += 1
        elif headX > tailX and headY < tailY:
            tailX += 1
            tailY -= 1
        elif headX > tailX and headY > tailY:
            tailX += 1
            tailY += 1
    
    visited.add((tailX, tailY))


for x in file:
    move = x.strip().split(" ")
    for i in range(int(move[1])):
        if move[0] == 'R':
            headX += 1
        elif move[0] == 'L':
            headX -= 1
        elif move[0] == 'U':
            headY -= 1
        elif move[0] == 'D':
            headY += 1
        updateTail() 

print(len(visited))
