num = input()

ans = float(num)

number =  num.split(".")
digit = number[1]
if int(digit[-1]) == 7:
    ans += 0.02
elif int(digit[-1]) % 2 == 1:
    ans -= 0.09
elif int(digit[-1]) > 7:
    ans -= 4
elif int(digit[-1]) < 4:
    ans += 6.78

digit = int(str(ans).split(".")[0])
decimal = int(str(ans).split(".")[1])

if(decimal < 10):
    decimal = str(decimal)+"0"
print(str(digit)+"."+str(decimal))