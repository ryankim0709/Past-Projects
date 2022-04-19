hms = input().split()
h, m, s = int(hms[0]),int(hms[1]),int(hms[2])
print(str(h), str(m), str(s) + ".", end="")
if h * s >= m:
    print(" I will make it")
else:
    print(" I will be late")
    
