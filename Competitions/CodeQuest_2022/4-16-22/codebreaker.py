cases = int(input())

for i in range(cases):
    total = 0
    lines = int(input())
    letters = {

    }
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alpha:
        letters[i] = 0
    for i in range(lines):
        line = input().lower()
        for j in line:
            if j not in alpha:
                continue
            else:
                total += 1
                letters[j] += 1

    for i in alpha:
        final = str(round((float(letters[i])/float(total))*float(100.0),2))
        percent = str(round((float(letters[i])/float(total))*float(100.0),2)).split(".")[1]
        
        if len(percent) == 1:
            final += "0"
        if len(percent) == 0:
            final += "00"
        print(i.upper()+": "+final+"%")