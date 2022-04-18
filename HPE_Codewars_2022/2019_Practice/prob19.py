def getKey(password):
	key = 0
	add = True
	for ltr in password:
		i = ord(ltr)
		if i < 32:
			while i < 32:
				i += 32
		elif i > 126:
			while i > 126:
				i -= 16
		if add:
			key += i
		else:
			key -= i
		add = not add
	return key

key = getKey(input())
inlist = []
a = input()
while a != "":
	inlist.append(a)
	a = input()

outlist = []
for thing in inlist:
	curout = []
	for letter in thing:
		curout.append(hex(ord(letter)*key))
	outlist.append(curout)

print(outlist)
