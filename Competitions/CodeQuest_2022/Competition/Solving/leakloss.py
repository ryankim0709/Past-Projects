n = int(input())
res = []
for i in range(n):
    data = input().split()
    volume = float(data[0])
    fillRate = float(data[1])
    leavingRate = float(data[2])

    waste = float(volume/(fillRate - leavingRate))
    waste = float(waste * leavingRate)
    #print(volume, fillRate, leavingRate, waste)
    res.append((int(round(waste))))

for r in res:
    print(r)