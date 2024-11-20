def longestValidParentheses(s):
    sList = list(s)
    print(s)
    longestPar = 0
    counter = 0

    while len(sList) > 1:
        compCheck = False
        i = 0

        if len(sList) == 2:
            if sList[0] + sList[1] == "()":
                counter += 2
                del sList[1]
                del sList[0]
            elif sList[0] + sList[1] == ")(" or sList[0] + sList[1] == "((" or sList[0] + sList[1] == "))":
                del sList[1]
                del sList[0]

        elif sList[i] + sList[i+1] == "()":
            counter +=2
            del sList[i+1]
            del sList[i]

        else:
            while i < len(sList)-2: #)()
                if sList[0] + sList[i+2] == "()" and sList[i+1] + sList[i+2] != "()":
                    del sList[i+2]
                    del sList[0]
                    counter += 2
                    compCheck = True
                    break
                i += 1

            if not compCheck:
                print("deleted!")
                del sList[0]
                counter = 0

        print(sList)
        print(counter)
        if counter > longestPar:
            longestPar = counter
    return longestPar

print(longestValidParentheses
      ("()(()))()()()()))()()()()()()"))

