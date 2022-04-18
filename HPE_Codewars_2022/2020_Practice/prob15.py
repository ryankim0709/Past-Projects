a, b = map(int, input().split())
print("\n")
while a != 0:
	sen1 = input()
	sen2 = input()
	s1 = set()
	for thing in sen1.split():
		s1.add(thing.lower())
	s2 = set()
	for thing in sen2.split():
		s2.add(thing.lower())
	duplicates = ""
	for word in s1:
		if word in s2:
			duplicates += word
			duplicates += " "
	print(sen1 + "\n" + sen2)
	print(f"{len(duplicates.split())} {duplicates.strip()}")
	a, b = map(int, input().split())