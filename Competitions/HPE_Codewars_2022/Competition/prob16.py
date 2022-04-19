def add2(a,b):
    sum = a + b
    if sum < 97:
        return add2(sum,b)
    else:
        return sum
def add2Call(a, b):
    return add2(ord(a), ord(b))

def getThing(o):
    if o > 122:
        return getThing(o-26)
    else:
        return chr(o)

def getCode(message):
    first4ord = []
    for i in range(4):
        first4ord.append(add2Call(message[i],message[i-1]))
    
    last4ord = []
    for i in range(-4, 0):
        last4ord.append(add2Call(message[i],message[i-1]))

    code = ""
    for i in first4ord:
        code += getThing(i)
    for i in last4ord:
        code += getThing(i)
    return code

message = input()
codein = input()

code = getCode(message)

if code == codein:
    print(codein + " equals " + codein)
    print("Gru")
else:
    print(code + " does not equal " + codein)
    print("Not Gru")

