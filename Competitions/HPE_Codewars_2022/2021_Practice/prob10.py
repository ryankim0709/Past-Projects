villagers = []

thing = input()
while thing != "END":
	split = thing.split()
	name = split[0][9:11]
	hours, mins = map(int, split[1].split(":"))
	vpf = int(split[2])*10
	villagers.append([name, hours, mins, vpf])
	thing = input()

tastyList = []
for villager in villagers:
	name, hours, mins, vpf = villager

	mins += vpf % 60
	hours += vpf//60

	if mins >= 60:
		hours += 1

	if hours < 17:
		tastyList.append(name)

	# print(name, hours, mins, vpf)
if len(tastyList) == 0:
	print("Blah, blah, blah, time to order delivery")
else:
	print(f"Villagers {tuple(tastyList)} look tasty")