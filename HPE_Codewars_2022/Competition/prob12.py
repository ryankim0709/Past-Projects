import math
numMats = int(input())
needed = list(map(int, input().split()))
has = list(map(int, input().split()))

numBridges = -1

for i in range(numMats):
    if has[i]/needed[i] > numBridges:
        numBridges = math.ceil(has[i]/needed[i])

for i in range(numMats):
    needMat = needed[i] * numBridges
    print(needMat - has[i], end=" ")