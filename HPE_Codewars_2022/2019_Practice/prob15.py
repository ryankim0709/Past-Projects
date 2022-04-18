

from tkinter import N

import math
inputs = input().split()
numCandles = int(inputs[0])
numBooks = int(inputs[1])

def slotCount(n, s):
    num = 1
    for i in range(s):
        num *= n-i 
    return num

def choose(n, r):
    return int(math.factorial(n) / (math.factorial(r)*math.factorial((n-r))))

ans = 0 


for candleCount in range(1, numCandles+1):
    if candleCount >= 4:
        break
    for bookCount in range(1, numBooks+1):
        if candleCount+bookCount > 4:
            break
        ans += choose(numCandles,candleCount) * choose(numBooks,bookCount)
        

        
print(ans)



'''
for every slot
items * items - 1 * items - 2 3
4 items, 2 slots 
ab ac ad 
ba bc bd 
ca cb cd 
da db dc 
'''
