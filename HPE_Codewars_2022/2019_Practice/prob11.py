width, height = map(int, input().split())

thinglist = []
for i in range(height):
	thing = input()
	y, skyline = thing[0], thing[1:]
	thinglist.append((y, skyline))

thinglist.sort()
print(thinglist)