numDict = {"1/4":0.25, "1/3":1/3, "1/2":0.5, "1":1, "2":2,"3":3}

sticks, size, tolerate = input().split()

if float(tolerate) >= float(sticks) * numDict[size] * 0.45 * 7.5:
	print(f"{str(round(float(sticks)*numDict[size]*0.45*7.5, 2))} the MASK can eat it!")
else:
	print(f"{str(round(float(sticks)*numDict[size]*0.45*7.5,2))} the MASK should not eat it!")