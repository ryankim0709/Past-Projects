num = int(input())

power = [0, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

idx = 12
powerTen = power[idx]

ans = {} # Key:power value:amount

while idx > 0:
    powerTen = power[idx]
    while(10 ** powerTen < num):
        if powerTen not in ans:
            ans[powerTen] = 1
        else:
            ans[powerTen] += 1
        num -= 10 ** powerTen
    idx -= 1


nums = {0:"zero", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

dataDict = {0: "", 1:"deca", 2: "hecto", 3:"kilo",6:"mega", 9:"giga", 12:"tera", 15:'peta',18:"exa", 21:"zetta", 24:'yotta', 27:'bronto', 30:'gego'}
finalString = ""

keyList = sorted(list(ans.keys()), reverse=True)
print(ans)
final = ""
for i in range(0, len(keyList)):
    power = keyList[i]
    repeats = ans[power]
    write = ""
    if repeats > 100:
        print(str(repeats[0]))
        write = str(repeats[0]) +" and"
        repeats -= int(str(repeats[0])) * 100
    if repeats > 10:
        write += str(repeats[0]) +"ty"
        repeats -= int(str(repeats[0])) * 10
    if repeats > 0:
        write += nums[repeats]
    
print(write)
    #final += nums[repeats]+" "+dataDict[power]+"bytes"+", "

if(len(keyList) == 0):
    print(nums[num] +" bytes")
else:
    final = final[0: len(final) - 2] + " and "+nums[num]+" bytes"
    print(final)
