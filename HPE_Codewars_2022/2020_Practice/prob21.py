name = input()
out = ""
while name != "":
	name = name.split()[1]
	rate = float(input().split()[1])
	a = input().split()[1]
	in1 = int(a[:2])*60+int(a[2:])
	a = input().split()[1]
	out1 = int(a[:2])*60+int(a[2:])
	a = input().split()[1]
	in2 = int(a[:2])*60+int(a[2:])
	a = input().split()[1]
	out2 = int(a[:2])*60+int(a[2:])

	total = rate*(out1-in1+out2-in2)/60
	out += f"{name} made ${total:.2f}\n"

	name = input()

print(out)