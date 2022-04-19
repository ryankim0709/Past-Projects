def do(command, ownername, curtemp, myname):
	command = command.split()
	if command[0] == "Hey":
		command = command[2:]
	# print(command)
	if "added" in command or "plus" in command:
		return (f"{command[1]} plus {command[-1][:-1]} is {int(command[1]) + int(command[-1][:-1])}, {ownername}", curtemp, myname, ownername)
	elif "times" in command or "multiplied" in command:
		return (f"{command[1]} times {command[-1][:-1]} is {int(command[1]) * int(command[-1][:-1])}, {ownername}", curtemp, myname, ownername)
	elif 'power?' in command:
		return (f"{command[1]} to the power of {command[-2][:-2]} is {int(command[1]) ** int(command[-2][:-2])}, {ownername}", curtemp, myname, ownername)
	elif "cold" in command or "up" in command:
		return (f"Temperature has been raised, {ownername}", int(curtemp) + 1, myname, ownername)
	elif "hot" in command or "down" in command:
		return (f"Temperature has been lowered, {ownername}", int(curtemp) - 1, myname, ownername)
	elif "current" in command:
		return (f"Current temperature is {curtemp}, {ownername}", curtemp, myname, ownername)
	elif "call" in command and "me" in command:
		return (f"Okay, I'll call you Dave from now on", curtemp, myname, "Dave")
	elif "your" in command and "name?" in command:
		return (f"My name is {myname}, {ownername}", curtemp, myname, ownername)
	elif "call" in command and "you"  in command:
		return (f"Okay, you can call me Computer from now on", curtemp, "Computer", ownername)
	elif "tell" in command and "joke" in command and "better" not in command:
		return (f"So this guy, a squirrel, and a dog walk into a bar...", curtemp, myname, ownername)
	elif "tell" in command and "joke" in command and "better" in command:
		return ("No", curtemp, myname, ownername)
	elif "pod" in command and "bay" in command:
		return (f"I can't do that, {ownername}", curtemp, myname, ownername)
	else:
		return (f"I don't understand you, {ownername}", curtemp, myname, ownername)

temp = int(input().split()[-1])
owner = input().split()[-1]
aiName = input().split()[-1]
a = input()
outlist = []
while a != "":
	(out, temp, aiName, owner) = do(a, owner, temp, aiName)
	outlist.append(out)
	a = input()

for thing in outlist:
	print(thing)