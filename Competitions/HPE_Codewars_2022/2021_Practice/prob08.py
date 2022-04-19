data = input().split()
height = int(data[0])
punch = int(data[1])
anger = int(data[2])

if(punch > height or punch == 0):
    for x in range(height):
        print("#")

else:
    for x in range(punch - 2):
        print("#")
    print("#", end = "")

    for x in range(int(anger/10)):
        print(".", end = "")
    for x in range(height - punch + 1):
        print("#", end = "")

    