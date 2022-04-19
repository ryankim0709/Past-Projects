tme = input()
outstr = ""
while tme != "":
	hours, mins = map(int, tme.split(":"))
	hours = hours%12
	hourDegs = hours*30 + mins*0.5
	minDegs = mins*6
	outstr += f"\nThe angle between the Hour hand and the Minute hand is {min(abs(hourDegs-minDegs), 360-abs(hourDegs-minDegs)):.2f} degrees."
	tme = input()
print(outstr)
