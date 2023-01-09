file = open("input.txt", "r")

data = []
dp = []
for x in file:
    data.append([])
    dp.append([])
    for c in x:
        if c.isnumeric():
            dp[-1].append(False)
            data[-1].append(int(c))

width  = len(data)
height = len(data[0])

max = 0
for r in range(width):
    for c in range(height):
        upVal = 0
        for up in range(r - 1, -1, -1):
            upVal += 1
            if data[r][c] <= data[up][c]:
                # print("UP",r, c)
                break

        downVal = 0 
        for down in range(r + 1, width):
            
            downVal += 1
            if data[r][c] <= data[down][c]:
                # print("DOWN",r, c)
                break
        
        leftVal = 0
        for left in range(c - 1, -1, -1):
            
            leftVal += 1
            if data[r][c] <= data[r][left]:
                # print("LEFT",r, c)
                break

        rightVal = 0
        for right in range(c + 1, height):
            
            rightVal += 1
            if data[r][c] <= data[r][right]:
                # print("RIGHT",r, c)
                break
        
        if leftVal * rightVal * upVal * downVal > max:
            # print("PROCESS",r, c)
            max = leftVal * rightVal * upVal * downVal
print(max)

'''
# FIRST PART
for r in range(width):
    max = -1
    for c in range(height):
        if data[r][c] > max:
            dp[r][c] = True
            max = data[r][c]
    max2 = -1
    for c in range(height - 1, 0, -1):
        if data[r][c] > max2:
            dp[r][c] = True
            max2 = data[r][c]


for c in range(height):
    max = -1
    for r in range(width):
        if data[r][c] > max:
            dp[r][c] = True
            max = data[r][c]
    max2 = -1
    for r in range(width - 1, 0, -1):
        if data[r][c] > max2:
            dp[r][c] = True
            max2 = data[r][c]



sum = 0
for r in dp:
    for c in r:
        if c:
            sum += 1

print(sum)
'''