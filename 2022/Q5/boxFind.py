'''
            [J] [Z] [G]            
            [Z] [T] [S] [P] [R]    
[R]         [Q] [V] [B] [G] [J]    
[W] [W]     [N] [L] [V] [W] [C]    
[F] [Q]     [T] [G] [C] [T] [T] [W]
[H] [D] [W] [W] [H] [T] [R] [M] [B]
[T] [G] [T] [R] [B] [P] [B] [G] [G]
[S] [S] [B] [D] [F] [L] [Z] [N] [L]
 1   2   3   4   5   6   7   8   9 

'''
boxes = [
    ["S","T","H","F","W","R"],
    ["S","G","D","Q","W"],
    ["B","T","W"],
    ["D","R","W","T","N","Q","Z","J"],
    ["F","B","H","G","L","V","T","Z"],
    ["L","P","T","C","V","B","S","G"],
    ["Z","B","R","T","W","G","P"],
    ["N","G","M","T","C","J","R"],
    ["L","G","B","W"]
]

file = open("input.txt", "r")
for x in file:
    vals = x.split(' ')
    
    a = int(vals[1])
    b = int(vals[3]) - 1
    c = int(vals[5]) - 1
    '''
    bLen = len(boxes[b])
    for i in range(a):
        boxes[c].append(boxes[b][bLen - a + i])
    for i in range(a):
        boxes[b].pop()
    '''
    rev = []
    print(boxes[b])
    print(a,boxes[b][-a:])
    for i in range(a):
        rev.append(boxes[b].pop())
    rev.reverse()
    print(boxes[b])
    print(boxes[c],rev)
    boxes[c].extend(rev)
    print(boxes[c])
    print()
    # boxes[c].extend(boxes[b][-a:])
    # boxes[b] = boxes[b][:-a]
    '''
    for i in range(a):
        boxes[c].append(boxes[b].pop())
    '''
word = []
for x in boxes:
    word.append(x[-1])
print("".join(word))
file.close()