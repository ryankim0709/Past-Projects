from operator import truediv


def doesWork(lst, start, rhymeLength):
    idx = start
    use = lst.copy()
    for i in range(len(lst) - 1):
        for j in range(rhymeLength - 1):
            idx += 1
            if idx == len(use):
                idx = 0
        del use[idx]
        if idx == len(use):
            idx = 0
        else:
            idx += 1
    if 1 in lst:
        return True
    return False

# n = int(input())

# for i in range(n):
#     data = input().split()
#     people = int(data[0])
#     rhyme = int(data[1])

#     for j in range(people):
#         if doesWork([i+1 for i in range(people)], j, rhyme):
#             print(j+1)
#             break

print(doesWork([i+1 for i in range(5)], 4, 16))