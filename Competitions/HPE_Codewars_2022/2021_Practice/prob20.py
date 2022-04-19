n = int(input())

towerList = []
for i in range(n):
	height, addr = input().split()
	towerList.append((int(height), addr))
towerList.sort()
tallest = towerList[-1][0]

for i in range(tallest, -1, -1):
	row = ""
	for tower in towerList:
		if tower[0] == i:
			row += "~"
		elif tower[0] > i:
			row += "*"
		elif i == 0:
			row += tower[1]
		else:
			row += " "
	print(row)

row =""
for tower in towerList:
	row += tower[1]
print(row)