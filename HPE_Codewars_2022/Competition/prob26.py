from platform import java_ver


width = int(input())
height = int(input())

forest = []
for i in range(height):
    forest.append(input().strip())

trees = []
for i in range(height):
    for j in range(width):
        if forest[i][j] != "x": # It's a tree
            trees.append((i,j, int(forest[i][j])))

fallenDict = {}

for (x,y, z) in trees:
    for i in range(z): # up
        stufflist = [(max(x - i, 0),y), (min(x + i, height - 1),y),(x,min(y + i, width - 1)),(x,max(y - i, 0 - 1))]
        for thing in stufflist:
            if thing in fallenDict:
                a = sorted([(x+1,y+1), fallenDict[thing][0]])
                print(a)
                break
            else:
                fallenDict[thing] = [(x+1,y+1)]



            
