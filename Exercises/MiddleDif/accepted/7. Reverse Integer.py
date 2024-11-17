
def reverse(self ,x):
    strX = str(x) # -3120
    newStr = ""
    isNegative = False
    devBy0 = False

    if x == 0:
        return 0

    if x < 0:
        isNegative = True
        newStr = strX.replace("-" ,"") # 3120
        strX = newStr
        x = int(newStr)

    if x % 10 == 0:
        devBy0 = True
        newStr = str(int(strX.rstrip('0')))


    if not devBy0 and not isNegative:
        for i in range(len(strX)):
            newStr += strX[i]
    newStr2 = ""

    if isNegative:
        newStr2 = "-"

    for i in range(len(newStr) - 1, -1, -1):
        newStr2 += newStr[i]

    if int(newStr2) > 2147483647 or int(newStr2) < -2147483647:
        return 0
    return int(newStr2)