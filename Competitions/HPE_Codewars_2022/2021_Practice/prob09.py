minions = int(input())
sphere = float(input())
body = input().split() # Radius then height
store = input().split() # Length, width, height

pi = 3.1415926536
cockpit = 4/3 * pi * sphere ** 3
bodyNeed = pi * float(body[0]) ** 2 * float(body[1])
storage = 2 * float(store[0]) * float(store[1]) * float(store[2])/3
minNeed = minions * 1.2

print("Cockpit",round(cockpit, 2))
print("Body", round(bodyNeed, 2))
print("Pods", round(storage, 2))
print("Minions Need", round(minNeed,2))

total = cockpit + bodyNeed + storage - 2.2 - 4.1 - 12.1 - minNeed
print("PLAN ACCEPTED" if total > 0 else "PLAN REJECTED")
