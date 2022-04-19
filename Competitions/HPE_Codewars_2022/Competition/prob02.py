evens = []
odds = []

while True:
    inp = int(input())
    if inp == 0:
        break
    elif inp % 2 == 0:
        evens.append(inp)
    elif inp % 2 == 1:
        odds.append(inp)

if len(evens) == 0 or len(odds) == 0:
    print("NO LIST PROBLEMS FOUND")
elif len(evens) > len(odds):
    print(odds[0], end=" ")
    print("is not even")
else:
    print(evens[0], end=" ")
    print("is not odd")
