

def longestValidParentheses(s):
    sList = list(s)
    longestPar = 0
    counter = 0
    theTruth = False
    theTruth3 = True
    while theTruth3:
        if (len(sList) == 2 and sList[0] + sList[1] == "((" or
            len(sList) == 2 and sList[0] + sList[1] == ")(" or
            len(sList) == 2 and sList[0] + sList[1] == "))"):
            if counter > longestPar:
                longestPar = counter
            break
        i = 0

        if sList[i] + sList[i+1] == "()":
            del sList[i+1]
            del sList[i]
            print(sList)
            counter += 2
            if len(sList) < 2:
                if counter > longestPar:
                    longestPar = counter
                break

        else:
            currentIndex = i
            while i < len(sList)-2:
                if sList[i+1] + sList[i+2] != "()" and sList[currentIndex] + sList[i+2] == "()":
                    del sList[i+2]
                    del sList[currentIndex]
                    counter += 2
                    theTruth = True
                    break
                i += 1
            i = 0
            if theTruth:
                theTruth = False
                continue
            #ako ne sme ospeli da namerim:
            if counter > longestPar:
                longestPar = counter
            i += 1
            counter = 0

        if i == len(s)-1:
            break
        if len(sList) < 2:
            theTruth3 = False
    return longestPar

print(longestValidParentheses("))(("))
