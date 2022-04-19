def getOption(list, num):
    while(len(list) != 1):
        list.pop(getRemove(len(list), num))
    return list[0]

def getRemove(size, num):
    curr = -1
    
    for i in range(num):
        curr += 1
        if curr == size:
            curr = -1
    return curr

amount = int(input())

options = []
names = []

for i in range(4):
    list = []
    names.append(input().split()[:-1])
    for j in range(amount):
        list.append(input())
    options.append(list)

input()
number = int(input())

print("Your MASH Story:")
for i in names:
    name = ""
    for j in i:
        name = name + str(j) + " "
    name = name[:-1]
    
    print(name+" - ",end="")
    print(getOption(options[0], number))
    options.pop(0)

    