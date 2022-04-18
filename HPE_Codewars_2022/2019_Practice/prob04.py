n = int(input())

taxlist = []
pricelist = []

outlist = []

for i in range(n):
	tax_rate = float(input())/100
	total = float(input())
	pretax = total / (1 + tax_rate)
	taxamount = pretax * tax_rate
	outlist.append((total, taxamount))

for (total, taxamount) in outlist:
	print(f"On your ${total} purchase, the tax amount was ${taxamount:.2f}.")
