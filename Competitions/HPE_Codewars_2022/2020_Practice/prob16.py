in_ = input()
while in_ != "":
	a, b, operation, ans = in_.split()
	opDict = {"DIVIDE": "/", "MULTIPLY": "*", "ADD": "+", "SUBTRACT": "-",
	          "POWER": "**"}
	operation = opDict[operation]

	if eval(a + operation + b) == float(ans):
		print(f"{ans} is correct for {float(a)} {operation if operation != '**' else '^'} {float(b)}")
	else:
		print(f"{float(a)} {operation if operation != '**' else '^'} {float(b)} = {str(round(eval(a+operation+b), 1)) + '.0' if int(round(eval(a+operation+b), 1)) == round(eval(a+operation+b), 1) else round(eval(a+operation+b), 1)} not {ans}")
	in_ = input()
