n = int(input())

for i in range(n):
    data = input().split()
    hex = data[0]
    order = data[1]

    if(order == "LITTLE"):
        p1 = hex[0] + hex[1]
        p2 = hex[2] + hex[3]
        p3 = hex[4] + hex[5]
        p4 = hex[6] + hex[7]
        hex = p4 + p3 + p2 + p1
    print(int(hex, 16))