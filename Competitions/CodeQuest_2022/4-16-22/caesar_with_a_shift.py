cases = int(input())

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(cases):
    toShift = input().lower()
    shifts = input().split()
    shiftSide = input().split()

    final = []

    now = 0
    for j in range(len(toShift)):
        let = toShift[j]
        if toShift[j] not in alpha:
            now -= 1
            final.append(toShift[j])
        else:
            amount = int(shifts[now % len(shifts)])
            side = int(shiftSide[now % len(shiftSide)])
            if side == 0: # Right
                final.append(alpha[(alpha.index(let) + amount) % len(alpha)])
            else:
                final.append(alpha[(alpha.index(let) - amount) % len(alpha)])
        now += 1
    for j in final:
        print(j,end="")
    print()