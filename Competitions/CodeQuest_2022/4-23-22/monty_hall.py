n = int(input())

def updateList(lst, playerInd, hostInd):
    minus = sum(lst[0:playerInd]) * -1
    doors = hostInd - playerInd + 1
    percent = (100.0 - float(minus))/float(doors)
    for i in range(playerInd, hostInd + 1):
        lst[i] = percent

for i in range(n):
    data = input().split()
    doors = int(data[0])
    rounds = int(data[1])
    opened = int(data[2])

    game = [100.0/doors for i in range(doors)]
    guestInd = 0
    hostInd = len(game) - 1

    for j in range(rounds):
        game[guestInd] *= -1
        guestInd += 1
        for j in range(opened):
            game[hostInd - j] = 0
        hostInd -= opened
        updateList(game, guestInd, hostInd)
    ans = str(round(max(game), 2))
    temp = ans.split(".")[1]
    if len(temp) == 0:
        ans += "00"
    elif len(temp) == 1:
        ans += "0"
    ans += "%"
    print(ans)