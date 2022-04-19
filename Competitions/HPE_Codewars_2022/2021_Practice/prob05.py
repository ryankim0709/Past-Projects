n = int(input())

inlist = []
for i in range(n):
	inlist.append(input())

dupes = []
bdays = []

for bday in inlist:
	newBday = bday[:5]
	if newBday in bdays:
		if newBday not in dupes:
			dupes.append(newBday)
	else:
		bdays.append(newBday)

if len(dupes) == 0:
	print(f"0\nduplicates: None")
else:
	outstring = ""
	for dupe in dupes:
		outstring += f" {dupe}"
	print(f"{len(dupes)}\nduplicates:{outstring}")
