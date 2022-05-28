def printSentence(sentence, dictionary):
    index = {
        'N':-1,
        'C':-1,
        'V':-1,
        'J':-1,
        'B':-1,
        'P':-1
    }
    final = ""
    nextInd = 0
    for i in sentence:
        nextInd = 0
        curr = ""
        type = i[0]

        if type == "Q":
            curr = "What "
        
        code = i[1:]

        for j in code:
            nextInd += 1
            if j == "T":
                curr += "the "
            elif j == "A":
                nextCode = code[nextInd]
                nextIndex = int(index[nextCode] + 1) % len(dictionary[nextCode])
                if dictionary[nextCode][nextIndex][0] in ('a','e','i','o','u'):
                    curr += "an "
                curr += "a "
            else:
                ind = int(index[j] + 1) % len(dictionary[j])
                curr += dictionary[j][ind] + " "
                index[j] = ind
        
        curr = curr[:-1]
        if type == "D" or type == "I":
            curr = curr + "."
        elif type == "Q":
            curr = curr + "?"
        elif type == "E":
            curr = curr + "!"
        final += curr[0].upper() + curr[1:] + " "
    print(final[:-1])


def main():
    lines = int(input())
    dictionary = {
        'N':[],
        'C':[],
        'V':[],
        'J':[],
        'B':[],
        'P':[]
    }

    for i in range(lines):
        data = input()
        dictionary[data[0]] = data[2:].split()
    
    printSentence(input().split(), dictionary)

main()