from math import trunc


def reverse(x):
    strX = str(x)
    newStr = ""
    newStr2 = ""
    isNegative = False
    devidedBy0 = False
    if x < 0:
        isNegative = True
        newStr = strX.replace("-","")

    elif x % 10 == 0:
        devidedBy0 = True
        newStr = strX.replace("0", "")

    #if no problems newstr2 is empty

    if isNegative:
        newStr2 = "-"
    if devidedBy0:
        for i in range(len(newStr) - 1, -1, -1):
            newStr2 += newStr[i]

    if not devidedBy0 and not isNegative:
        for i in range(len(strX) - 1, -1, -1):
            newStr2 += strX[i]
    return int(newStr2)

print(reverse(-123))