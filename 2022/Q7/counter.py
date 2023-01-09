file = open("input.txt", "r")

class Node:
    def __init__(self):
        self.directories = dict()
        self.size = 0
        self.parent = None 
    
    def moveTo(self, name : str):
        if name == "..":
            print("..")
            return self.parent
        else:
            
            if name in self.directories:
                return self.directories[name]
            else:
                newNode = Node()
                newNode.parent = self
                self.directories[name] = newNode
                return newNode

curr = Node()
root = curr
for line in file:
    line = line.strip()
    parts = line.split(" ")
    print(parts)
    if parts[0] == "$":
        if parts[1] == "cd":
            curr = curr.moveTo(parts[2])
        else:
            continue
    else:
        if parts[0].isnumeric():
            curr.size += int(parts[0])


def addDirectories(currNode):
    for x in currNode.directories.keys():
        # print(x)
        addDirectories(currNode.directories[x])
        currNode.size += currNode.directories[x].size

def findSmallest(currNode, needed):
    val = currNode.size
    for x in currNode.directories.keys():
        if currNode.directories[x].size < needed:
            continue
        val = min(val, findSmallest(currNode.directories[x], needed))
    return val
    

addDirectories(root)
print(findSmallest(root, 30000000 -(70000000 - root.size)))