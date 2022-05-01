import itertools

n = int(input())

for i in range(n):
    bits = int(input())
    lst = [list(i) for i in itertools.product([0, 1], repeat=bits)]
    for j in range(len(lst)):
        final = ""
        for k in range(bits):
            final += str(lst[j][k])
        print(final)