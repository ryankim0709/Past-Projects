


teams = {}
for i in range(4):
    teams[input().strip()] = [0,0] # points, goaldiff

for i in range(6):
    a, score, b = input().split()
    ascore, bscore = score.split(":")
    ascore = int(ascore)
    bscore = int(bscore)
    if int(ascore) > int(bscore):
        teams[a][0] += 3
        teams[a][1] += ascore - bscore
        teams[b][1] += bscore - ascore
    elif int(ascore) < int(bscore):
        teams[b][0] += 3
        teams[a][1] += ascore-bscore
        teams[b][1] += bscore - ascore
    else:
        teams[a][0] += 1
        teams[b][0] += 1

final = {}
for team in sorted(list(teams.keys()), key=lambda x: teams[x][0],reverse=True):
    if teams[team][0] in final:
        final[teams[team][0]].append([team, teams[team][0], teams[team][1]])

    else:
        final[teams[team][0]]= [[team, teams[team][0], teams[team][1]]]

order = []
for key in sorted(list(final.keys()), reverse=True):
    mylist = final[key]
    mylist.sort(key=lambda x: x[2], reverse=True)
    order += mylist

for a, b, c in order:
    print(f"{a} {b} {c}")
