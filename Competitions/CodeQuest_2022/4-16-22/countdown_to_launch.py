import math

def works(data):
    date = data[0]
    time = data[1]
    cloud_thick = int(data[2])
    windspeed = float(data[3])
    degrees = int(data[4])
    windEW = math.fabs(math.sin(degrees / 180.0 * math.pi)) * windspeed
    windNS = math.fabs(math.cos(degrees / 180.0 * math.pi)) * windspeed

    if cloud_thick > 1000:
        return False
    elif windEW > 40:
        return False
    elif windNS > 20:
        return False
    else:
        print(date+" "+time)
        return True

n = int(input())

for i in range(n):
    times = int(input())
    solved = False
    
    for j in range(times):
        res = input().split()
        if not solved:
            res = works(res)
        if not solved and res == True:
            solved = True
    if solved == False:
        print("ABORT LAUNCH")

    


