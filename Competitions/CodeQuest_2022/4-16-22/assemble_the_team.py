def findOptimal(agents):
    p1 = 0
    p2 = 0
    final = []
    while p2 < len(agents) - 1:
        if agents[p2 + 1][1] - agents[p1][1] <= 10:
            p2 += 1
        else:
            p1 += 1
        length = p2 - p1 + 1

        if length > len(final):
            now = []
            for i in range(p1, p2 + 1):
                now.append(agents[i][0])
            final = now.copy()
        elif length == len(final):
            now = []
            for i in range(p1, p2 + 1):
                now.append(agents[i][0])
            now.sort()
            final.sort()

            for i in range(len(final)):
                if ord(now[i]) < ord(final[i]):
                    final = now.copy()
                elif ord(now[i]) > ord(final[i]):
                    break
    return final


cases = int(input())
last = False
for i in range(cases):
    if i == cases - 1:
        last = True
    data = input().split()

    agents = []
    for j in data:
        j = j.split("=")
        agents.append((j[0], int(j[1])))
    agents.sort(key = lambda x:x[1])
    print(' '.join(findOptimal(agents)), end="")
    if last == False:
        print()
    