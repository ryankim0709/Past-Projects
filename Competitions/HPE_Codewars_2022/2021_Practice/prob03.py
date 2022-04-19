thing = input()
while thing != "":
	inlist.append(thing)
	thing = input()

found = False
for y, row in enumerate(inlist):
	for x, column in enumerate(row):
		if column == "P":
			print(f"Ace, move fast, pigeon is at ({x},{y})")
			found = True

if found == False:
	print("No pigeon, try another map, Ace")