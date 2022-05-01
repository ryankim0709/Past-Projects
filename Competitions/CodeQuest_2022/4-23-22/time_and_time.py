n = int(input())

for i in range(n):
    case = input()
    case = case.replace("and", "")
    case = case.replace(",", "")
    case = case.replace(" ","")

    for j in range(len(case)):
        if case[j] == "m" or case[j] == "h" or case[j] == "s":
            case = case[0:j + 1] + " " + case[j + 1:len(case)]
    case = case.split()
    
    hour = "00"
    minute = "00"
    seconds = "00"

    for j in case:
        type = j[-1]
        if type == "h":
            hour = j[0:len(j)-1]
        elif type == "s":
            seconds = j[0:len(j)-1]
        else:
            minute = j[0:len(j)-1]
        
        if len(hour) == 1:
            hour = "0"+hour
        if len(minute) == 1:
            minute = "0"+minute
        if len(seconds) == 1:
            seconds = "0"+seconds
    print(hour+":"+minute+":"+seconds)