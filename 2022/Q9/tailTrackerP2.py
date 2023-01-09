file = open("input.txt", "r")

stringList = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = set()

def updateTail(idx : int):
    global stringList
    
    prevX = stringList[idx - 1][0]
    prevY = stringList[idx - 1][1]

    currX = stringList[idx][0]
    currY = stringList[idx][1]

    if abs(currX - prevX) <= 1 and abs(currY - prevY) <= 1:
        return

    xDiff = 1 if prevX > currX else -1 if prevX < currX else 0
    yDiff = 1 if prevY > currY else -1 if prevY < currY else 0

    stringList[idx][0] += xDiff
    stringList[idx][1] += yDiff


for x in file:
    move = x.strip().split(" ")
    for i in range(int(move[1])):
        if move[0] == 'R':
            stringList[0][0] += 1
        elif move[0] == 'L':
            stringList[0][0] -= 1
        elif move[0] == 'U':
            stringList[0][1] -= 1
        elif move[0] == 'D':
            stringList[0][1] += 1
        
        for i in range(1,10):
            updateTail(i) 
        
        visited.add((stringList[-1][0], stringList[-1][1]))
print(stringList)
print(len(visited))
