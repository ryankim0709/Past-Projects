n = int(input())

for i in range(n):
    data = input().split(":")
    speed = float(data[0])
    distance = float(data[1])

    if(speed >= distance):
        print("SWERVE")
    elif(speed * 5.0 >= distance):
        print("BRAKE")
    elif(speed * 5.0 < distance):
        print("SAFE")