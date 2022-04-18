num = input()
ans = 0

count = 0

while(num != 0):
    ans = 0

    count = 0
    for i in range(0, len(num)):
        ans += 3 ** count * int(num[len(num) - i - 1]) 
        count += 1
    
    num = input()
    print(ans)
