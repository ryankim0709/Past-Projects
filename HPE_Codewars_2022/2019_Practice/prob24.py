inurl = input()

out = ""
encoding = True
slashcount = 0
for ltr in inurl:
	if not ltr.isalnum():
		if ltr == '/':
			slashcount += 1
		if slashcount == 3:
			encoding = True
		if encoding:
			out += f"0x25{hex(ord(ltr))[2:]}"
		else:
			out += ltr
		if slashcount == 2:
			encoding = False

	else:
		out += ltr
print(out)

