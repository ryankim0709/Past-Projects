def fib2(preprev, prev, target):
	outlist = [preprev, prev]
	for i in range(2, target):
		outlist.append(outlist[i-1]+outlist[i-2])
	return outlist
a = int(input())
b = int(input())
c = int(input())

print(",".join(str(x) for x in fib2(a, b, c)))