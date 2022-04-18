contestants = []
names = []
for i in range(2):
    inp = input().split()
    names.append(inp[-1])
    inp.remove(inp[-1])
    for t in range(6):
        inp[t] = int(inp[t])
    contestants.append(inp)

for contestant in range(5):
    score = 0
    for i in range(2):
        newScore = contestants[contestant][i*2]
        newScore -= contestants[contestant][i*2+1]
        if newScore < 0:
            newScore = 0
    score+=newScore
    print(names[contestant],end=" ")
    print(score)