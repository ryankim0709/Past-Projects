F = input().split()
K = input().split()
X = input().split()

if F[1] == "?":
    ans = -1 * float(K[1]) * float(X[1])
    print("F",round(ans, 2))

elif K[1] == "?":
    ans = -1 * float(F[1])/float(X[1])
    print("K",round(ans,2))

else:
    ans = -1 * float(F[1])/float(K[1])
    print("X", round(ans,2))