words = input().split()

outlist = []
prevWordList = [words[0]]
streak = 1
for word in words[1:]:
	if word.lower() == prevWordList[0].lower():
		streak += 1
		prevWordList.append(word)
	else:
		if prevWordList[0].lower() not in ['is', 'had']:
			outlist.append(prevWordList[0])
		else:
			outlist += prevWordList[:2]
		streak = 1
		prevWordList = [word]
if streak == 1 or prevWordList[0].lower() not in ['is', 'had']:
	outlist.append(prevWordList[0])
else:
	outlist += prevWordList[:2]
print(" ".join(outlist))