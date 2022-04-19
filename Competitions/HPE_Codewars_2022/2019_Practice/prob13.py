first = input()
second = input()
third = input()
four = input()

if first == "X":
    print(round((float(second) * float(third)) / float(four),1))
elif second == "X":
    print(round((float(first) * float(four)) / float(third),1))
elif third == "X":
    print(round((float(first) * float(four)) / float(second),1))
else:
    print(round((float(second) * float(third)) / float(first),1))