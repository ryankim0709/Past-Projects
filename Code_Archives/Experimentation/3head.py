import random


def oneTrial():
    flip1 = random.randint(0, 1) == 1
    flip2 = random.randint(0, 1) == 1
    flip3 = random.randint(0, 1) == 1

    numFlips = 3

    while not(flip1 and flip2 and flip3):
        flip1 = flip2
        flip2 = flip3
        flip3 = random.randint(0, 1) == 1
        numFlips += 1

    return numFlips


sum = 0
count = 0

while count < 1000:
    sum += oneTrial()
    count += 1

print(sum/count)