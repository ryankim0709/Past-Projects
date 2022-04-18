letters = input()
ltrDict = {}
for letter in letters:
	if letter == " ":
		letter = '_'
	if letter in ltrDict:
		ltrDict[letter] += 1
	else:
		ltrDict[letter] = 1

lessthan10 = []
morethan10 = []
for thing in ltrDict:
	if ltrDict[thing] < 10:
		lessthan10.append((ord(thing), thing))
	else:
		morethan10.append((ord(thing), thing))

lessthan10.sort(reverse=True)
morethan10.sort()

out = ""
for (order, letter) in lessthan10:
	out += f"{letter}[{ltrDict[letter]}]"
out += ';'
for (order, letter) in morethan10:
	out += f"{letter}[{ltrDict[letter]}]"
print(out)

