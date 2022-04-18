name = input()
peopleNeeded = int(input())
minsCanRun = int(input())
secsToStart = int(input())
output = round(float(input())/3600, 2)
canPeople = int(input())

canDo = True

if output < 121000000000:
	canDo = False

if minsCanRun*60 - 1 >= secsToStart and canDo and canPeople >= peopleNeeded:
	print(f"{name} can generate {output} watts per second")
	print("MARTY CAN MAKE IT!")
else:
	print(f"{name} can generate {0.00} watts per second")
	print("WOAH, HEAVY!")