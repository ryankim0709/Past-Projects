message = input()
paren = 0
numLeft = 0
numRight = 0
balanced = True
numPairs = 0

for i in message:
    if i == "(":
        parent = 1
        numLeft += 1
    elif i == ")":
        paren -= 1
        numRight += 1
        if paren < 0:
            balanced = False
        else:
            numPairs += 1

print("Total left: " + str(numLeft))
print("Total right: " + str(numRight))
print("Total pairs: " + str(numPairs))
if balanced:
    print("Balanced")
else:
    print("Unbalanced")
