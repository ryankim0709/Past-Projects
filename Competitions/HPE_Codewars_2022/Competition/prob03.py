data = input().split()
pts = int(data[0])
fga = int(data[1])
fta = int(data[2])

ts = round(100 * pts/(2*(fga + (0.44 * fta))),2)
print(str(ts)+"%")