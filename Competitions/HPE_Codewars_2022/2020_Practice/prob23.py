n = int(input())
upsideDownDict = {"o": "o", "x": "x", "s": "s", "z": "z",
                  "a": 'e', 'b': 'q', 'd': 'p', 'h': 'y', 'm': 'w', 'n': 'u',
                  'e': 'a', 'q': 'b', 'p': 'd', 'y': 'h', 'w': 'm', 'u': 'n'}

for i in range(n):
	s = input().lower()
	news = ""
	k = ""
	for ch in reversed(s):
		if ch in upsideDownDict:
			k += upsideDownDict[ch]
			news += ch
		if ch == ' ':
			k += ' '
			news += ' '
	upside = True

	for j in range(len(news)):
		if news[j] == " ":
			continue
		print(upsideDownDict[k[j]])
		if news[j] != upsideDownDict[k[j]]:
			upside = False
			break
	news = news[::-1]
	print(news, "|", k, "|", upside)
	# if upside:
	# 	print(f"{news} (is) {k}")
	# else:
	# 	print(f"{news} (not) {k}")
