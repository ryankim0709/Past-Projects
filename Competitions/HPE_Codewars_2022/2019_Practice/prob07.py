import math

def isPrime(num):
    for i in range(2, int(num/2)+1):
        if num%i==0:
            return False
    return True

while True:
    nums = input().split()
    num = int(nums[0])
    action = int(nums[1])
    if action == 0:
        if num%2==0:
            print(num)
        else:
            print(num+1)
    if action == 1:
        nextPrime = num 
        while True:
            if isPrime(nextPrime):
                print(nextPrime)
                break    
            nextPrime += 1
    if action == 2:
        isSquare = False 
        nextSquare = num 
        while not isSquare:
            if math.sqrt(nextSquare).is_integer():
                print(nextSquare)
                isSquare = True
            nextSquare+= 1
    if action == 3:
        for i in range(1, num):
            if i * i * i >= num:
                print(i*i*i)
                break 
