inStr = input()
startch = inStr[0]

staches = [x.split(startch) for x in inStr.split()]

start = staches[0][1]
prev = None
# print(staches)
for i in range(1, len(staches)):
    # print(start, staches[i][1], prev)
    if staches[i][1] != start:
        # print("Not equal to start")
        if prev == None:
            if staches[i+1][1] == start:
                print(f'#{i+1} {startch}{staches[i][1]}{startch} you are you of control!')
                break
            else:
                print(f'#{1} {startch}{staches[0][1]}{startch} you are you of control!')
                break
        else:
            if prev == start:
                print(f'#{i+1} {startch}{staches[i][1]}{startch} you are you of control!')
                break
            else:
                print(f'#{1} {startch}{staches[0][1]}{startch} you are you of control!')
                break
    prev = staches[i][1]

