conversion = {"MILES": 1609.34, "KILOMETERS": 1000,
			  "YARDS":0.9144, "FEET": 0.3048, "INCHES": 0.0254,
			  "METERS": 1.0, "CENTIMETERS": 0.01}

timeConversion = {"HOUR": 1/3600, "MINUTE": 1/60, "SECOND": 1}

thing = input().split()

name = thing[0]
number = float(thing[1])
convert = thing[2]
timeConvert = thing[4]

mps = number*conversion[convert]*timeConversion[timeConvert]

height = round(mps**2 /(2*9.805),2)

if 25 <= height <= 50:
	print(f"{name} will launch the messenger {height} meters high, SUCCESS!")

elif 25 > height:
	print(f"{name} will launch the messenger {height} meters high, SPLAT!")
else:
	print(f"{name} will launch the messenger {height} meters high, OUCH!")