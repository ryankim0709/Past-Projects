key = {'F':'A',
'G':'B',
'H':'C',
'I':'D',
'J':'E',
'K':'F',
'L':'G',
'M':'H',
'N':'I',
'O':'J',
'P':'K',
'Q':'L',
'R':'M',
'S':'N',
'T':'O',
'U':'P',
'V':'Q',
'W':'R',
'X':'S',
'Y':'T',
'Z':'U',
'A':'V',
'B':'W',
'C':'X',
'D':'Y',
'E':'Z',}

n = int(input())
inString = input()
outstring = ""
for ltr in inString:
	if ltr in key:
		outstring += key[ltr]
	else:
		outstring += ltr
print(outstring)